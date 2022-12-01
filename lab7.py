from abc import ABC, abstractmethod
import random

rna_nucl = ['C', 'A', 'U', 'G']
dna_nucl = ['C', 'A', 'T', 'G']

class NA(ABC):
    def __init__(self, chain, nucl, chein_qua):
        self.chain = chain
        self.nucl = nucl
        self.chein_qua = chein_qua
        
        
        for i in self.chain:                 #Рабтает 
            if i not in self.nucl:
                print('Exeption')
                print(self.chain, i, '- there is problem')
                break
                
    def compl(self):                       #работает
        compl_chain = ""                   
        for i in self.chain:
            for j in range(4):
                if i == self.nucl[j]:
                    compl_nucl = dna_nucl[3-j] 
            compl_chain += compl_nucl  
        return(compl_chain)
    
    
    @abstractmethod
    def create_na(self):
        pass
    
    @abstractmethod
    def na_i(self, i):
        pass
    
    @abstractmethod
    def __add__(self, other):
        pass
    
    def __eqq__(self, other):
        f = True
        if len(self.chain)!=len(other.chain):
            f = False
        else:    
            for i in range(len(self.chain)):
                if self.chain[i] != other.chain[i]:
                    f = False
                    break
        return (f)   
    
    
    def __mul__(self, other):
        mul_chain = ""
        diff = len(self.chain) - len(other.chain)
        
        for i in range (min(len(self.chain), len(other.chain))):
            mul_chain += random.choice([self.chain[i], other.chain[i]])
            a = len(mul_chain)
        
        for i in range (a, a + abs(diff)):
            if (diff > 0):
                mul_chain += self.chain[i]
            else:
                mul_chain += other.chain[i]
        
        
        if(type(self) == '<class \'__main__.RNA\'>'):
            mul_na  = RNA(chain = mul_chain) 
        else:
            mul_na  = DNA(chain = mul_chain) 

        
        return mul_na.create_na()        
    
    @abstractmethod
    def __str__( self ):
        pass                           
    
    
class RNA(NA):
    
    def __init__(self, chain):
            super().__init__(chain=chain, nucl=rna_nucl, chein_qua=1)
            
    def create_na(self):
            return(self.chain)
 
        
    def __add__(self, other):                     #Рабтает
            return (self.chain + other.chain)    
        
    def na_i(self,i):
            return(self.chain[i-1])
        
    def __str__( self ):
            return self.chain
        
      
            
            
            

        
rna1 = RNA(chain = "AAUACG")      
rna2 = RNA(chain = "UCA")

print( rna1.compl() )

    
    
class DNA(NA):
        def __init__(self, chain):
            super().__init__(chain=chain, nucl=dna_nucl, chein_qua=2)
            
        def create_na(self):
            return([self.chain, self.compl()])

                    
        
        def __add__(self, other):
            new_dna = []
            for i in range (2):
                new_dna[i] = self.create_na()[i] + other.create_na()[i]
            return (new_dna)
        
        def na_i(self, i):
            return([self.create_na()[0][i-1], self.create_na()[1][i-1]])
        
        def __str__( self ):
            return "["+ self.create_na()[0] + ", "+  self.create_na()[1]+ "]"
       
                    

                    
dna1 = DNA(chain = "TATCG")     
dna2 = DNA(chain = "AAAAAAAAA")
        
              
