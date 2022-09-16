import math
import os
import requests
from lxml import html

from v1.modules.page_manager import PageManager
from v1.modules.utils import parseNumber


class Routine():
    def __init__(self):
        self.driver = PageManager()

    def run(self, user, password):
        self.driver.open_url("https://ceiapp.b3.com.br/CEI_Responsivo/")

        for val in user:  # typing letter by letter because the site doesn't work with word
            self.driver.find('//*[@id="ctl00_ContentPlaceHolder1_txtLogin"]', "xpath").send_keys(val, delay_before=0.2,
                                                                                                 delay_after=0)
        for val in password:  # typing letter by letter because the site doesn't work with word
            self.driver.find('//*[@id="ctl00_ContentPlaceHolder1_txtSenha"]', "xpath").send_keys(val, delay_before=0.2,
                                                                                                 delay_after=0)
        self.driver.find('//*[@id="ctl00_ContentPlaceHolder1_btnLogar"]', "xpath").click(delay_after=0.5)
        self.driver.find('//*[@id="ctl00_ContentPlaceHolder1_sectionCarteiraAtivos"]/p/a', "xpath").click(
            delay_after=0.3)
        self.driver.find('//*[@id="ctl00_ContentPlaceHolder1_repTabelaAtivos_ctl03_LinkButton2"]', "xpath").click()

        list_portfolio = []
        company_elements = self.driver.findall(
            '//*[@id="ctl00_ContentPlaceHolder1_rptAgenteContaMercado_ctl00_rptContaMercado_ctl00_rprCarteira_ctl00_grdCarteira"]/tbody/tr/td[1]',
            "xpath")
        type_elements = self.driver.findall(
            '//*[@id="ctl00_ContentPlaceHolder1_rptAgenteContaMercado_ctl00_rptContaMercado_ctl00_rprCarteira_ctl00_grdCarteira"]/tbody/tr/td[2]',
            "xpath")
        code_elements = self.driver.findall(
            '//*[@id="ctl00_ContentPlaceHolder1_rptAgenteContaMercado_ctl00_rptContaMercado_ctl00_rprCarteira_ctl00_grdCarteira"]/tbody/tr/td[3]',
            "xpath")
        value_elements = self.driver.findall(
            '//*[@id="ctl00_ContentPlaceHolder1_rptAgenteContaMercado_ctl00_rptContaMercado_ctl00_rprCarteira_ctl00_grdCarteira"]/tbody/tr/td[5]',
            "xpath")
        qtde_elements = self.driver.findall(
            '//*[@id="ctl00_ContentPlaceHolder1_rptAgenteContaMercado_ctl00_rptContaMercado_ctl00_rprCarteira_ctl00_grdCarteira"]/tbody/tr/td[6]',
            "xpath")
        total_value_elements = self.driver.findall(
            '//*[@id="ctl00_ContentPlaceHolder1_rptAgenteContaMercado_ctl00_rptContaMercado_ctl00_rprCarteira_ctl00_grdCarteira"]/tbody/tr/td[8]',
            "xpath")

        for company, type_, value, code, qtde, total_value in zip(company_elements, type_elements, code_elements,
                                                                  value_elements, qtde_elements, total_value_elements):
            list_portfolio.append(
                {"company": company.text, "type": type_.text, "value": value.text, "code": code.text, "qtde": qtde.text,
                 "totalValue": total_value.text})
        return list_portfolio
