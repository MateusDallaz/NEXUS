from fastapi import FastAPI;

app = FastAPI();

@app.get("/usuario")
def usuario_rota():
    return {
        "usuario_uuid": "1",
        "nome": "Pedro",
        "email": "pedro@example.com",
        "senha_hash": "12345",
        "avatar_url": "https://example.com/avatar.jpg",
        "status": "ativo",
        "criado_em": "2026-07-21",
        "ultimo_login_em": "2026-07-21"
        }


@app.get("/servidor")
def servidor_rota():
    return {"servidor_uuid": "1",
            "nome": "Pedro",
            "descrição": "teste",
            "icone_url": "...",
            "dono_uuid": "p&dro",
            "publico": "pedro_gat",
            "criado_em": "2026/06/20"
            }

@app.get("/categoria_canal")
def categoria_canal_rota():
    return {
        "cateegoria_uuid": "1",
        "servidor_uuid": "1",
        "nome": "Teste",
        "posicao": "1"
    }

@app.get("/membro_servidor")
def membro_servidor_rota():
    return {
        "membro_uuid": "1",
        "usuario_uuid": "1",
        "servidor_uuid": "1",
        "cargo_uuid": "1",
        "data_entrada": "2026-07-21",
    }

@app.get("/convite")
def convite_rota():
    return {
        "convite_uuid": "1",
        "servidor_uuid": "1",
        "criado_por_uuid": "1",
        "codigo": "abcd123",
        "usos_maximos": "50",
        "usos_atuais": "15",
        "expira_em": "2026-08-21"
    }

@app.get("/canal")
def canal_rota():
    return {
        "canal_uuid": "1",
        "servidor_uuid": "1",
        "categiria_uuid": "1",
        "nome": "teste",
        "tipo": "texto",
        "posicao": "1"
    }
    
@app.get("/reacao")
def reacao_rota():
    return {
        "reacao_uuid": "1",
        "mensagem_uuid": "1",
        "usuario_uuid": "1",
        "emoji": "=D",
        "criado_em": "2026-07-21"
    }

@app.get("/anexo")
def anexo_rota():
    return {
        "mensagem_uuid": "1",
        "url_arquivo": "https://claude.ai/chat/e25d5a1d-1c72-4781-8376-deef21e58bb6",
        "tipo_arquivo": "teste",
        "tamanho_bytes": "12375"
    }



@app.get("/cargo")
def cargo_rota():
    return {"cargo_uuid": "1",
            "servidor_uuid": "1",
            "nome": "Pedro",
            "cor": "verde",
            "permissoes": "adm",
            "posicao": "lider"
    }
    
@app.get("/Banimento")
def banimento_rota():
    return {"banimento_uuid": "01",
            "servidor_uuid": "1",
            "usuario_uuid": "Carlos",
            "banido_por_uuid": "Diego P",
            "motivo": "Racismo",
            "criado_em": "2026/06/01"
    }  

@app.get("/mensagem")
def menssagem_rota():
    return {"menssagem_uuid": "Teste",
            "usuario_uuid": "Marcos W",
            "canal_uuid": "Chat",
            "conteudo": "Denúncia",
            "tipo": "online",
            "fixada": "SIM",
            "criado_em": "2026/06/02",
            "editado_em": "2026/06/03"
    }


        




    