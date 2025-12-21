/**
 * Класс для управления задачами
 */
export class TaskManager {
    constructor() {
        this.tasks = this.loadTasks();
    }

    /**
     * Загрузка задач из локального хранилища
     * @returns {Array} Массив задач
     */
    loadTasks() {
        try {
            const data = localStorage.getItem('tasks');
            return data ? JSON.parse(data) : [];
        } catch (error) {
            console.error('Ошибка загрузки задач:', error);
            return [];
        }
    }

    /**
     * Сохранение задач в локальное хранилище
     */
    saveTasks() {
        try {
            localStorage.setItem('tasks', JSON.stringify(this.tasks));
        } catch (error) {
            console.error('Ошибка сохранения задач:', error);
        }
    }

    /**
     * Добавление новой задачи
     * @param {string} title - Название задачи
     * @param {string} description - Описание задачи
     * @returns {Object} Созданная задача
     */
    addTask(title, description = '') {
        const task = {
            id: Date.now(),
            title,
            description,
            completed: false,
            createdAt: new Date().toISOString()
        };

        this.tasks.push(task);
        this.saveTasks();
        return task;
    }

    /**
     * Получение всех задач
     * @param {boolean} showCompleted - Показывать завершенные задачи
     * @returns {Array} Отфильтрованный массив задач
     */
    getAllTasks(showCompleted = true) {
        return showCompleted 
            ? this.tasks 
            : this.tasks.filter(task => !task.completed);
    }

    /**
     * Поиск задачи по ID
     * @param {number} id - ID задачи
     * @returns {Object|null} Найденная задача или null
     */
    getTaskById(id) {
        return this.tasks.find(task => task.id === id) || null;
    }

    /**
     * Обновление статуса задачи
     * @param {number} id - ID задачи
     * @param {boolean} completed - Новый статус
     * @returns {boolean} Успешность операции
     */
    toggleTaskCompletion(id) {
        const task = this.getTaskById(id);
        if (task) {
            task.completed = !task.completed;
            task.updatedAt = new Date().toISOString();
            this.saveTasks();
            return true;
        }
        return false;
    }

    /**
     * Удаление задачи
     * @param {number} id - ID задачи
     * @returns {boolean} Успешность операции
     */
    deleteTask(id) {
        const initialLength = this.tasks.length;
        this.tasks = this.tasks.filter(task => task.id !== id);
        
        if (this.tasks.length !== initialLength) {
            this.saveTasks();
            return true;
        }
        return false;
    }

    /**
     * Получение статистики по задачам
     * @returns {Object} Статистика
     */
    getStatistics() {
        const total = this.tasks.length;
        const completed = this.tasks.filter(task => task.completed).length;
        const pending = total - completed;

        return {
            total,
            completed,
            pending,
            completionRate: total > 0 ? (completed / total * 100).toFixed(1) : 0
        };
    }
}

/**
 * Утилиты для работы с консолью
 */
export class ConsoleUtils {
    /**
     * Вывод цветного текста в консоль
     * @param {string} text - Текст для вывода
     * @param {string} color - Цвет текста
     */
    static colorLog(text, color) {
        const colors = {
            reset: '\x1b[0m',
            red: '\x1b[31m',
            green: '\x1b[32m',
            yellow: '\x1b[33m',
            blue: '\x1b[34m',
            magenta: '\x1b[35m',
            cyan: '\x1b[36m'
        };

        console.log(`${colors[color] || colors.reset}${text}${colors.reset}`);
    }

    /**
     * Создание горизонтальной линии
     * @param {number} length - Длина линии
     * @returns {string} Горизонтальная линия
     */
    static createLine(length = 50) {
        return '─'.repeat(length);
    }

    /**
     * Форматирование даты
     * @param {string} isoString - Дата в формате ISO
     * @returns {string} Отформатированная дата
     */
    static formatDate(isoString) {
        const date = new Date(isoString);
        return date.toLocaleString('ru-RU');
    }
}