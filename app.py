import streamlit as st
from crud import criar_aluno,listar_alunos,atualizar_idade,deletar_aluno

st.set_page_config(page_title="Gerenciamento de alunos", page_icon="👨‍🎓")

st.title("Sistemas de alunos com PostgreSQL")

menu = st.sidebar.radio("Menu", ["Inserir", "Listar", "Atualizar", "Deletar"])

if menu == "Inserir":
    st.subheader("➕Inserir alunos")
    nome = st.text_input("Nome", placeholder="Seu nome")
    idade = st.number_input("Idade", min_value=16, step=1)
    if st.button("Cadastrar"):
        if nome.strip() != "":
            criar_aluno(nome, idade)
            st.success(f"Aluno {nome} inserido com sucesso!")
        else:
            st.warning("O campo nome não pode ser vazio.")
elif menu == "Listar":
    st.subheader("Listar alunos")
    alunos = listar_alunos()
    if alunos:
        st.dataframe(alunos)
    else:
        st.info("Nenhum aluno encontrado.")
elif menu == "Atualizar":
    st.subheader("Atualizar idade")
    alunos = listar_alunos()
    if alunos:
        id_aluno = st.selectbox("Escolha o id do aluno para " \
        "atualizar", [linha[0] for linha in alunos])
        nova_idade = st.number_input("Nova idade", min_value=16, step=1)
        if st.button("Atualizar idade"):
            atualizar_idade(id_aluno, nova_idade)
            st.success(f"Idade do aluno atualizada com sucesso.")
    else:
        st.info("Nenhum aluno disponivel para atualizar")