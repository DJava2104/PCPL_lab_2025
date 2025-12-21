"""
Простой скрипт для запуска всех тестов
"""
import subprocess
import sys
import os

def main():
    print("ЗАПУСК ВСЕХ ТЕСТОВ")
    print("=" * 60)
    
    # Список тестов для запуска
    tests = [
        ("TDD тесты", ["py", "test_calculator_tdd.py"]),
        ("Mock тесты", ["py", "test_calculator_mock.py"]),
        ("BDD тесты", ["py", "-m", "behave", "features/"])
    ]
    
    results = []
    
    for test_name, command in tests:
        print(f"\n{test_name}:")
        print("-" * 40)
        
        try:
            # Запускаем тесты
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            
            # Выводим результат
            print(result.stdout)
            if result.stderr:
                print("Ошибки:", result.stderr)
            
            success = result.returncode == 0
            results.append((test_name, success))
            
        except FileNotFoundError as e:
            print(f"Ошибка: {e}")
            print("Убедитесь, что Python установлен и доступен как 'py'")
            results.append((test_name, False))
        except Exception as e:
            print(f"Ошибка при запуске тестов: {e}")
            results.append((test_name, False))
    
    # Итоговый отчет
    print("\n" + "=" * 60)
    print("ИТОГИ:")
    print("=" * 60)
    
    all_passed = True
    for test_name, success in results:
        status = "✓ ПРОЙДЕН" if success else "✗ НЕ ПРОЙДЕН"
        print(f"{test_name}: {status}")
        if not success:
            all_passed = False
    
    print("=" * 60)
    
    if all_passed:
        print("ВСЕ ТЕСТЫ УСПЕШНО ПРОЙДЕНЫ!")
    else:
        print("НЕКОТОРЫЕ ТЕСТЫ НЕ ПРОЙДЕНЫ!")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)