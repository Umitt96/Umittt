class BankaCuzdan:
    def __init__(self,yıllıkFaizOranı=2.5,yılSayısı=1,borç=1000,borçlu=""):
        self.__yıllıkFaizOranı=yıllıkFaizOranı
        self.__yılSayısı=yılSayısı
        self.__borç=borç
        self.__borçlu=borçlu

    def getYıllıkFaizOranı(self):
        return self.__yıllıkFaizOranı

    def getYılSayısı(self):
        return self.__yılSayısı

    def getBorç(self):
        return self.__borç

    def getBorçlu(self):
        return self.__borçlu

    def setYıllıkFaizOranı(self, yıllıkFaizOranı):
        self.__yıllıkFaizOranı=yıllıkFaizOranı
        
    def setYılSayısı(self, yılSayısı):
        self.__yılSayısı=yılSayısı


    def setBorç(self, borç):
        self.__borç=borç


    def setBorçlu(self, borçlu):
        self.__borçlu=borçlu
        

    def getAylıkÖdeme(self):
        aylıkFaizOranı=self.__yıllıkFaizOranı/1200
        aylıkÖdeme=self.__borç*aylıkFaizOranı/(1-(1/
                (1+aylıkFaizOranı)**(self.__yılSayısı*12)))
        return aylıkÖdeme

    def getToplamÖdeme(self):
        toplamÖdeme=self.getAylıkÖdeme()*self.__yılSayısı*12
        return toplamÖdeme
        












    
    
