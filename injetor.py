from db import Base
from sqlalchemy import Column, Integer, String

class Injetor(Base):
    __tablename__ = 'injetores'

    id = Column(Integer, primary_key=True)
    fabricante = Column(String)
    codigo = Column(String)
    tipo = Column(String)
    pd_ddp_maior = Column(Integer)
    pd_ddp_menor = Column(Integer)
    pr_ddp = Column(Integer)
    pd_ml_maior = Column(Integer)
    pd_ml_menor = Column(Integer)
    pr_ml = Column(Integer)
    pd_cp_maior = Column(Integer)
    pd_cp_menor = Column(Integer)
    pr_cp = Column(Integer)
    pd_pc_maior = Column(Integer)
    pd_pc_menor = Column(Integer)
    pr_pc = Column(Integer)
    pd_pi_maior = Column(Integer)
    pd_pi_menor = Column(Integer)
    pr_pi = Column(Integer)

    pressao_ddp = Column(Integer)
    pulso_ddp = Column(String)
    injetadas_ddp = Column(Integer)
    frequencia_ddp = Column(Integer)
    
    pressao_ml = Column(Integer)
    pulso_ml = Column(String)
    injetadas_ml = Column(Integer)
    frequencia_ml = Column(Integer)
    
    pressao_cp = Column(Integer)
    pulso_cp = Column(String)
    injetadas_cp = Column(Integer)
    frequencia_cp = Column(Integer)
    
    pressao_pc = Column(Integer)
    pulso_pc = Column(String)
    injetadas_pc = Column(Integer)
    frequencia_pc = Column(Integer)
    
    pressao_pi = Column(Integer)
    pulso_pi = Column(String)
    injetadas_pi = Column(Integer)
    frequencia_pi = Column(Integer)

    def __str__(self):
        return f'''
            Fabricante: {self.fabricante}
            Código: {self.codigo}
            Tipo: {self.tipo}
            -------------------------------
            MARCHA LENTA
            -------------------------------
            Pressão: {self.pressao_ml}
            Pulso: {self.pulso_ml}
            Frequência: {self.frequencia_ml}
            Injetadas: {self.injetadas_ml}
        '''
    