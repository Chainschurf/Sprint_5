from selenium.webdriver.common.by import By


class ButtonsLocators:
    LOGOUT_BUTTON = By.XPATH, "//button[text()='Выход']" # Путь к кнопке выхода из аккаунта
    REGISTER_BUTTON = By.XPATH, "//button[text()='Зарегистрироваться']" # Путь к кнопке регистрации в окне регистрации
    ENTER_ACCOUNT_BUTTON = By.XPATH, "//button[text()='Войти в аккаунт']" # Путь к кнопке "Войти в аккаунт" на главной странице, когда пользователь разлогинен
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//p[text()='Личный Кабинет']/parent::a" # Путь к кнопке "Личный Кабинет"
    REGISTRATION_FORM_BUTTON = By.XPATH, "//p[text()='Уже зарегистрированы?']/a[text()='Войти']" # Путь к кнопке "Войти" из окна регистрации
    FROM_PASSWORD_RESTORE_BUTTON = By.XPATH, "//p[text()='Вспомнили пароль?']/a[text()='Войти']" # Путь к кнопке "Войти" из окна восстановления пароля
    PASSWORD_RESTORE_BUTTON = By.LINK_TEXT, "Восстановить пароль" # Путь к кнопке "Восстановить пароль" из окна входа
    MAKE_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']" # Путь к кнопке "Оформить заказ" на главной странице, когда пользователь залогинен
    LOGO_BUTTON = By.XPATH, "//header/nav/div/a" # Путь к кнопке-логотипу в хедере
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[text()='Конструктор']/parent::a" # Путь к кнопке "Конструктор" в хедере
    ENTER_BUTTON = By.XPATH, "//button[text()='Войти']" # Путь к кнопке "Войти" в окне логина
    REGISTER_INSTEAD_LINK = By.LINK_TEXT, "Зарегистрироваться" # Путь к кнопке "Зарегистрироваться" в окне логина


class SigningLocators:
    NAME_FIELD = By.XPATH, "//label[text()='Имя']/parent::div/input" # Путь к полю ввода имени
    EMAIL_FIELD = By.XPATH, "//label[text()='Email']/parent::div/input" # Путь к полю ввода электронной почты
    PASSWORD_FIELD = By.XPATH, "//input[@name='Пароль']" # Путь к полю ввода пароля
    WRONG_PASSWORD = By.XPATH, "//p[text()='Некорректный пароль']" # Путь к сообщению об ошибке для некорректного пароля


class ConstructorPageLocators:
    BULKI_TAB = By.XPATH, "//span[text()='Булки']/parent::div" # Путь ко вкладке "Булки" на главной странице
    SOUSY_TAB = By.XPATH, "//span[text()='Соусы']/parent::div" # Путь ко вкладке "Соусы" на главной странице
    NACHINKI_TAB = By.XPATH, "//span[text()='Начинки']/parent::div" # Путь ко вкладке "Начинки" на главной странице
    SOUSY_SELECTED = By.XPATH, "//span[text()='Соусы']/parent::div[contains(@class, 'tab_tab_type_current')]" # Путь к выбранной вкладке "Булки" на главной странице
    BULKI_SELECTED = By.XPATH, "//span[text()='Булки']/parent::div[contains(@class, 'tab_tab_type_current')]" # Путь к выбранной вкладке "Соусы" на главной странице
    NACHINKI_SELECTED = By.XPATH, "//span[text()='Начинки']/parent::div[contains(@class, 'tab_tab_type_current')]" # Путь к выбранной вкладке "Начинки" на главной странице
    BULKI_SECTION = By.XPATH, "//h2[text()='Булки']" # Путь к названию секции "Булки"
    SOUSY_SECTION = By.XPATH, "//h2[text()='Соусы']" # Путь к названию секции "Соусы"
    NACHINKI_SECTION = By.XPATH, "//h2[text()='Начинки']" # Путь к названию секции "Начинки"
    CONSTRUCTOR_PAGE = By.XPATH, "//h1[text()='Соберите бургер']" # Путь к тексту "Соберите бургер" на странице конструктора



