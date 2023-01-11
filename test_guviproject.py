import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

class TestOrangeHRM():

    @pytest.fixture()
    def setup(self):
        self.driver=webdriver.Edge()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        yield
        self.driver.close()

    def testLogin_TC_PIM_01(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        search_box=self.driver.find_element(By.XPATH,"//input[@placeholder='Search']")
        print(search_box.is_displayed())
        print(search_box.is_enabled())
        search_box.send_keys("admin")
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span").click()

    def testAdmin_TC_PIM_02(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        Admin_Link=self.driver.find_element(By.XPATH,"//span[normalize-space()='Admin']")
        print(Admin_Link.is_displayed())
        Admin_Link.click()

        #User Management
        self.driver.find_element(By.XPATH,"//span[normalize-space()='User Management']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//ul[@role='menu']//li").click()

        #Admin Select
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div").click()
        Element = self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]")
        for opt in Element:
            if opt.text == "Admin":
                opt.click()
                break

        #Enabled Select
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]").click()
        Status_Ele = self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]")
        for sta in Status_Ele:
            if sta.text == "Enabled":
                sta.click()
                break

        #ESS Select
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div").click()
        ess_Ele= self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]")
        for Es in ess_Ele:
            if Es.text=="ESS":
                Es.click()
                break

        #Disabled Select
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]").click()
        Status_dis = self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]")
        for sta_dis in Status_dis:
            if sta_dis.text == "Disabled":
                sta_dis.click()
                break

    def testPIM_TC_PIM_03(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        # PIM Details
        self.driver.find_element(By.XPATH,"//span[normalize-space()='PIM']").click()
        PIM_Ele=self.driver.find_element(By.XPATH, "//span[normalize-space()='PIM']")
        print(PIM_Ele.is_displayed())

        #+ADD Button
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()

        #Image Add
        # Image=self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/div/button/i")
        # Image.click()
        # time.sleep(3)
        #Image.send_keys("C:\SeleniumPractice\govind.jpg")

        # Add Employee
        self.driver.find_element(By.NAME, "firstName").send_keys("Srinidhi")
        self.driver.find_element(By.NAME, "lastName").send_keys("Magi")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//span[@class='oxd-switch-input oxd-switch-input--active --label-right']").click()

        # Create Login Details
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input").send_keys("Srinidhitm")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input").send_keys("Srinidhitm@123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input").send_keys("Srinidhitm@123")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

    def testPIM_TC_PIM_04(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        #My Info
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()

        Personal=self.driver.find_element(By.XPATH,"//a[normalize-space()='Personal Details']")
        print(Personal.is_displayed())
        print(Personal.is_enabled())
        Contact=self.driver.find_element(By.XPATH,"//a[normalize-space()='Contact Details']")
        print(Contact.is_displayed())
        Emergency=self.driver.find_element(By.XPATH,"//a[normalize-space()='Emergency Contacts']")
        print(Emergency.is_displayed())
        Dependents=self.driver.find_element(By.XPATH,"//a[normalize-space()='Dependents']")
        print(Dependents.is_displayed())
        Immigration=self.driver.find_element(By.XPATH,"//a[normalize-space()='Immigration']")
        print(Immigration.is_displayed())
        Job=self.driver.find_element(By.XPATH,"//a[normalize-space()='Job']")
        print(Job.is_displayed())
        print(Job.is_enabled())
        Salary=self.driver.find_element(By.XPATH,"//a[normalize-space()='Salary']")
        print(Salary.is_displayed())
        print(Salary.is_enabled())
        Tax=self.driver.find_element(By.XPATH,"//a[normalize-space()='Tax Exemptions']")
        print(Tax.is_displayed())
        print(Tax.is_enabled())
        Report=self.driver.find_element(By.XPATH,"//a[normalize-space()='Report-to']")
        print(Report.is_displayed())
        print(Report.is_enabled())
        Qualification=self.driver.find_element(By.XPATH,"//a[normalize-space()='Qualifications']")
        print(Qualification.is_displayed())
        Member=self.driver.find_element(By.XPATH,"//a[normalize-space()='Memberships']")
        print(Member.is_displayed())

    def testEmp_Personal_Details_05(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        #My Info
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()

        #Personal Details
        Emp_Name=self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input")
        Emp_Name.clear()
        time.sleep(3)
        Emp_Name.send_keys("Srinidhi Magi")

        Emp_Id=self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input")
        Emp_Id.clear()
        time.sleep(3)
        Emp_Id.send_keys("0270")

        #Nationality
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div").click()
        Nation=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[2]")
        for Nat in Nation:
            if Nat.text=="Afghan":
                Nat.click()
                break

        #Date of Birth
        time.sleep(5)
        Date=self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input")
        Date.clear()
        Date.send_keys("1997-01-28")

        #Smoker
        self.driver.find_element(By.XPATH,"//label[normalize-space()='Yes']").click()

        #Save Button
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button").click()

        #Blood Type
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div").click()
        Group=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div/div[2]")
        for Bld in Group:
            if Bld.text=="B+":
                Bld.click()
                break
        #Save Button
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button").click()

    def testEmp_Contact_Details_06(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        # My Info
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()

        #Contact Details
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Contact Details']").click()

        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("10 Street")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("Anna Nagar")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input").send_keys("Chennai")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input").send_keys("Tamil Nadu")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input").send_keys("600040")

        #Country Select
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div").click()
        Con=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[2]")
        for co in Con:
            if co.text=="Afghanistan":
                co.click()
                break

        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input").send_keys("123456")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input").send_keys("7777777777")
        Email=self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input")
        Email.clear()
        Email.send_keys("sri@gmail.com")
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()

    def testEmergency_Contact_Details_07(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        #My Info
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()
        #Emergency Contacts
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Emergency Contacts']").click()

        #Add Button
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button").click()

        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Suvedha")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("Friend")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input").send_keys("5555555555")
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()

    def testEmp_Dependents_ContactDetails_08(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        #My Info
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()

        #Dependents_ContactDetails
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Dependents']").click()

        #Add Button
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button").click()
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Athithi Sri")

        #DropDown
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div").click()
        Ele_Sel=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]")
        print(len(Ele_Sel))
        for Rel in Ele_Sel:
            if Rel.text=="Child":
                Rel.click()
                break

        #Date of Birth
        time.sleep(3)
        Cdate=self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div/div/div[2]/div/div/input")
        Cdate.click()
        Cdate.send_keys("2020-03-10")

        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()

    def testEmp_Job_Details_09(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        # My Info
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()

        #Qualifications
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Qualifications']").click()
        #Add Work Experiance
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div/button").click()
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Guvi Tech")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("Software Testing")

        #From Date
        Fdate=self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div/input")
        Fdate.click()
        Fdate.send_keys("2019-03-10")

        Tdate=self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div/input")
        Tdate.click()
        Tdate.send_keys("2022-10-10")

        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()

        #Education
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div/button").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div").click()
        Degree=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]")
        print(len(Degree))
        for de in Degree:
            if de.text=="Master's Degree":
                de.click()
                break
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("College Of Engg & Tech")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/form/div[1]/div/div[3]/div/div[2]/input").send_keys("B.Tech")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/form/div[1]/div/div[4]/div/div[2]/input").send_keys("2018")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/form/div[1]/div/div[5]/div/div[2]/input").send_keys("83%")

        #From Date
        EFdate=self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div/input")
        EFdate.click()
        EFdate.send_keys("2014-05-10")

        #To Date
        ETdate=self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div/input")
        ETdate.click()
        ETdate.send_keys("2018-05-11")
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()

    def testEmp_TC_MEM_10(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        # My Info
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()

        #Memberships
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Memberships']").click()

        #Add Button
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button").click()

        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div").click()
        Mem_Ele=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]")
        for mem in Mem_Ele:
            if mem.text=="ACCA":
                mem.click()
                break

        #Subscription
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div").click()
        Com_Ele=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]")
        print(len(Com_Ele))
        for co in Com_Ele:
            if co.text=="Company":
                co.click()
                break

        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input").send_keys("10000")
        #Currency
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div").click()
        Curr=self.driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]")
        for c in Curr:
            if c.text=="Afghanistan Afghani":
                c.click()
                break

        #Subscription Date
        Subdate=self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div/input")
        Subdate.click()
        Subdate.send_keys("2015-10-10")

        #Renewal Date
        Redate=self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/input")
        Redate.click()
        Redate.send_keys("2020-10-10")
        time.sleep(5)
        self.driver.find_element(By.TAG_NAME,"button").click()

    def testEmp_TC_REP_11(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        # My Info
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()
        #Report
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Report-to']").click()


    def testEmp_Salary_12(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        # My Info
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()
        #Salary
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Salary']").click()

    def testEmp_Tax_Exemptions_13(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        # My Info
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()
        #Tax Exemptions
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Tax Exemptions']").click()



































































