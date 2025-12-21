@echo off
echo ========================================
echo ЛАБОРАТОРНАЯ РАБОТА №5: ЗАПУСК ТЕСТОВ
echo ========================================

echo.
echo 1. Запуск TDD тестов...
echo ========================================
py test_calculator_tdd.py
if %errorlevel% neq 0 (
    echo TDD тесты не прошли!
    pause
    exit /b 1
)

echo.
echo 2. Запуск Mock тестов...
echo ========================================
py test_calculator_mock.py
if %errorlevel% neq 0 (
    echo Mock тесты не прошли!
    pause
    exit /b 1
)

echo.
echo 3. Запуск BDD тестов...
echo ========================================
py -m behave features/
if %errorlevel% neq 0 (
    echo BDD тесты не прошли!
    pause
    exit /b 1
)

echo.
echo ========================================
echo ВСЕ ТЕСТЫ УСПЕШНО ПРОЙДЕНЫ!
echo ========================================
pause