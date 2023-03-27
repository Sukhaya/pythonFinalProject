import time

from pages.AuthPage import AuthPage
from pages.CartPage import CartPage
from pages.MixersPage import MixersPage
from pages.ProductPage import ProductPage
from pages.ProfilePage import ProfilePage
from pages.StartPage import StartPage
from pages.SuccessAddPopup import SuccessAddPopup


def testBuy(browser):

    start_page = StartPage(browser)
    start_page.openUrl()
    start_page.openAuthPage()

    auth_page = AuthPage(browser)
    auth_page.assertCurrentUrl()
    auth_page.fillEmail()
    auth_page.fillPassword()
    auth_page.clickLogin()
    auth_page.doScreenshot()

    profile_page = ProfilePage(browser)
    profile_page.assertTitle()
    profile_page.openMenu()
    profile_page.chooseMixers()
    profile_page.doScreenshot()

    mixers_page = MixersPage(browser)
    mixers_page.assertCurrentUrl()
    mixers_page.openSeriaFilter()
    mixers_page.clickCheckBoxSeria()
    mixers_page.openPriceFilter()
    mixers_page.setMinPrice()
    mixers_page.setMaxPrice()
    mixers_page.selectMixer()

    product_page = ProductPage(browser)
    product_page.assertTitle()
    product_page.addToCart()
    product_page.doScreenshot()

    popup_page = SuccessAddPopup(browser)
    popup_page.getTitle()
    popup_page.goToCart()
    product_page.doScreenshot()

    cart_page = CartPage(browser)
    cart_page.assertTitle()
    cart_page.assertEmail()
    cart_page.fillDelivery()
    cart_page.selectPaymentCash()
    cart_page.acceptAgreement()
    time.sleep(5)
    cart_page.checkClickable()
    cart_page.doScreenshot()











