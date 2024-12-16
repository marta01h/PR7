// Устанавливаем конечную дату: 26 мая 2025 года
const targetDate = new Date('December 25, 2024 00:00:00').getTime();

// Обновляем таймер каждую секунду
const countdown = setInterval(function() {
    const now = new Date().getTime();  // Текущее время
    const timeRemaining = targetDate - now;  // Разница во времени

    // Вычисляем дни, часы, минуты и секунды
    const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

    // Отображаем результат в элементе с id="countdown"
    document.getElementById("countdown").textContent =
        days + "д " + hours + "ч " + minutes + "м " + seconds + "с ";

    // Если обратный отсчет завершился
    if (timeRemaining < 0) {
        clearInterval(countdown);
        document.getElementById("countdown").textContent = "Время истекло!";
    }
}, 1000);