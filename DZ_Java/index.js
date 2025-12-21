import { TaskManager, ConsoleUtils } from './taskManager.js';
import readline from 'readline';

/**
 * Основной класс приложения
 */
class TaskManagerApp {
    constructor() {
        this.taskManager = new TaskManager();
        this.rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });

        // Имитация localStorage для Node.js
        if (typeof localStorage === 'undefined') {
            this.initializeLocalStorage();
        }
    }

    /**
     * Инициализация локального хранилища для Node.js
     */
    initializeLocalStorage() {
        const localStorageMock = {
            data: {},
            setItem(key, value) {
                this.data[key] = value;
            },
            getItem(key) {
                return this.data[key] || null;
            },
            removeItem(key) {
                delete this.data[key];
            },
            clear() {
                this.data = {};
            }
        };

        global.localStorage = localStorageMock;
    }

    /**
     * Отображение главного меню
     */
    showMainMenu() {
        ConsoleUtils.colorLog('\n' + ConsoleUtils.createLine(), 'cyan');
        ConsoleUtils.colorLog('📋 МЕНЕДЖЕР ЗАДАЧ', 'cyan');
        ConsoleUtils.colorLog(ConsoleUtils.createLine(), 'cyan');
        ConsoleUtils.colorLog('1. Просмотреть все задачи', 'yellow');
        ConsoleUtils.colorLog('2. Добавить новую задачу', 'green');
        ConsoleUtils.colorLog('3. Отметить задачу как выполненную', 'blue');
        ConsoleUtils.colorLog('4. Удалить задачу', 'red');
        ConsoleUtils.colorLog('5. Показать статистику', 'magenta');
        ConsoleUtils.colorLog('6. Выход', 'reset');
        ConsoleUtils.colorLog(ConsoleUtils.createLine(), 'cyan');

        this.rl.question('\nВыберите действие (1-6): ', (answer) => {
            this.handleMenuChoice(answer.trim());
        });
    }

    /**
     * Обработка выбора пользователя
     * @param {string} choice - Выбор пользователя
     */
    handleMenuChoice(choice) {
        switch (choice) {
            case '1':
                this.showAllTasks();
                break;
            case '2':
                this.addNewTask();
                break;
            case '3':
                this.toggleTaskCompletion();
                break;
            case '4':
                this.deleteTask();
                break;
            case '5':
                this.showStatistics();
                break;
            case '6':
                this.exitApp();
                break;
            default:
                ConsoleUtils.colorLog('❌ Неверный выбор. Попробуйте снова.', 'red');
                this.showMainMenu();
                break;
        }
    }

    /**
     * Отображение всех задач
     */
    showAllTasks() {
        const tasks = this.taskManager.getAllTasks();
        
        ConsoleUtils.colorLog('\n' + ConsoleUtils.createLine(60), 'cyan');
        ConsoleUtils.colorLog('📝 СПИСОК ВСЕХ ЗАДАЧ', 'cyan');
        ConsoleUtils.colorLog(ConsoleUtils.createLine(60), 'cyan');

        if (tasks.length === 0) {
            ConsoleUtils.colorLog('Задачи не найдены.', 'yellow');
        } else {
            tasks.forEach(task => {
                const status = task.completed ? '✅' : '⭕';
                const color = task.completed ? 'green' : 'yellow';
                
                ConsoleUtils.colorLog(`\nID: ${task.id}`, color);
                ConsoleUtils.colorLog(`Статус: ${status} ${task.completed ? 'Выполнена' : 'В процессе'}`, color);
                ConsoleUtils.colorLog(`Заголовок: ${task.title}`, color);
                
                if (task.description) {
                    ConsoleUtils.colorLog(`Описание: ${task.description}`, color);
                }
                
                ConsoleUtils.colorLog(`Создана: ${ConsoleUtils.formatDate(task.createdAt)}`, color);
                
                if (task.updatedAt) {
                    ConsoleUtils.colorLog(`Обновлена: ${ConsoleUtils.formatDate(task.updatedAt)}`, color);
                }
                
                ConsoleUtils.colorLog(ConsoleUtils.createLine(40), color);
            });
        }

        this.showMainMenu();
    }

    /**
     * Добавление новой задачи
     */
    addNewTask() {
        ConsoleUtils.colorLog('\n' + ConsoleUtils.createLine(), 'green');
        ConsoleUtils.colorLog('➕ ДОБАВЛЕНИЕ НОВОЙ ЗАДАЧИ', 'green');
        ConsoleUtils.colorLog(ConsoleUtils.createLine(), 'green');

        this.rl.question('Введите заголовок задачи: ', (title) => {
            this.rl.question('Введите описание задачи (необязательно): ', (description) => {
                const task = this.taskManager.addTask(title.trim(), description.trim());
                
                ConsoleUtils.colorLog('\n✅ Задача успешно добавлена!', 'green');
                ConsoleUtils.colorLog(`ID задачи: ${task.id}`, 'green');
                
                this.showMainMenu();
            });
        });
    }

    /**
     * Изменение статуса задачи
     */
    toggleTaskCompletion() {
        this.rl.question('\nВведите ID задачи для изменения статуса: ', (id) => {
            const taskId = parseInt(id.trim());
            
            if (isNaN(taskId)) {
                ConsoleUtils.colorLog('❌ Неверный ID задачи.', 'red');
                this.showMainMenu();
                return;
            }

            const success = this.taskManager.toggleTaskCompletion(taskId);
            
            if (success) {
                ConsoleUtils.colorLog('✅ Статус задачи успешно обновлен!', 'green');
            } else {
                ConsoleUtils.colorLog('❌ Задача с указанным ID не найдена.', 'red');
            }
            
            this.showMainMenu();
        });
    }

    /**
     * Удаление задачи
     */
    deleteTask() {
        this.rl.question('\nВведите ID задачи для удаления: ', (id) => {
            const taskId = parseInt(id.trim());
            
            if (isNaN(taskId)) {
                ConsoleUtils.colorLog('❌ Неверный ID задачи.', 'red');
                this.showMainMenu();
                return;
            }

            const success = this.taskManager.deleteTask(taskId);
            
            if (success) {
                ConsoleUtils.colorLog('✅ Задача успешно удалена!', 'green');
            } else {
                ConsoleUtils.colorLog('❌ Задача с указанным ID не найдена.', 'red');
            }
            
            this.showMainMenu();
        });
    }

    /**
     * Отображение статистики
     */
    showStatistics() {
        const stats = this.taskManager.getStatistics();
        
        ConsoleUtils.colorLog('\n' + ConsoleUtils.createLine(), 'magenta');
        ConsoleUtils.colorLog('📊 СТАТИСТИКА ЗАДАЧ', 'magenta');
        ConsoleUtils.colorLog(ConsoleUtils.createLine(), 'magenta');
        
        ConsoleUtils.colorLog(`Всего задач: ${stats.total}`, 'magenta');
        ConsoleUtils.colorLog(`Выполнено: ${stats.completed}`, 'green');
        ConsoleUtils.colorLog(`В процессе: ${stats.pending}`, 'yellow');
        ConsoleUtils.colorLog(`Процент выполнения: ${stats.completionRate}%`, 'cyan');
        
        this.showMainMenu();
    }

    /**
     * Выход из приложения
     */
    exitApp() {
        ConsoleUtils.colorLog('\n👋 До свидания! Приложение закрывается...', 'cyan');
        this.rl.close();
        process.exit(0);
    }

    /**
     * Запуск приложения
     */
    run() {
        ConsoleUtils.colorLog('\n🚀 Запуск Менеджера задач...', 'green');
        ConsoleUtils.colorLog('Для работы приложения используется Node.js', 'yellow');
        ConsoleUtils.colorLog('Данные сохраняются в localStorage', 'yellow');
        
        this.showMainMenu();
    }
}

// Запуск приложения
const app = new TaskManagerApp();
app.run();