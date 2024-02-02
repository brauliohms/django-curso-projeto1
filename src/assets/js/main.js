// Obtém o nome da url atual
const path = window.location.pathname;
const cleanPath = path.replace("/escola", "");

// Obtém os elementos da navbar
const navHome = document.getElementById("home");
const navAlunos = document.getElementById("alunos");
const navDisciplinas = document.getElementById("disciplinas");

// Cria uma lista com os elementos da navbar para facilitar as ações
const pages = new Array(navHome, navAlunos, navDisciplinas);

// Faz um loop em todos os elementos:
pages.map((page) => {
    // e verifica se o elemento contem a classe active
    if (page.classList.contains("active")) {
        // Se tiver a classe active, remove
        page.classList.remove("active");
    }
    // Vefifica se o atributo name é igual a url
    if (page.name == cleanPath) {
        // se for igual adiciona a classe active
        page.classList.add("active");
    }
});
