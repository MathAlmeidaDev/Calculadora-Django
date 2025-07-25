// Seleciona o elemento HTML com id "display" (onde a operação e o resultado aparecem)
let display = document.getElementById("display");

// Adiciona um valor (número ou operador) ao display
function addToDisplay(value) {
    if (display.innerText === "0") {
        // Se o display estiver com "0", substitui pelo valor clicado
        display.innerText = value;
    } else {
        // Caso contrário, concatena o novo valor à expressão atual
        display.innerText += value;
    }
}

// Limpa o display e reseta para "0"
function clearDisplay() {
    display.innerText = "0";
}

// Inverte o sinal do número atual exibido no display
function toggleSign() {
    let value = parseFloat(display.innerText); // Converte o conteúdo do display para número
    if (!isNaN(value)) { // Verifica se é um número válido
        display.innerText = (-value).toString(); // Inverte o sinal e exibe
    }
}

// Calcula o resultado da expressão exibida no display
function calcular() {
    try {
        // Substitui os símbolos visuais (× e ÷) pelos operadores reais (* e /)
        let expressao = display.innerText.replace(/×/g, '*').replace(/÷/g, '/');
        let resultado = eval(expressao); // Usa eval() para calcular a expressão

        // Envia a operação para o backend Django usando método POST
        fetch("", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
                "X-CSRFToken": getCSRFToken() // Adiciona token CSRF para segurança
            },
            body: `expressao=${encodeURIComponent(expressao)}` // Envia a expressão no corpo da requisição
        }).then(() => {
            location.reload(); // Recarrega a página para atualizar o histórico
        });

        display.innerText = resultado; // Mostra o resultado no display
    } catch (e) {
        // Em caso de erro na expressão, mostra "Erro"
        display.innerText = "Erro";
    }
}

// Função que envia uma operação para o backend via JSON (não está sendo usada no momento)
function enviarParaDjango(operacao, resultado) {
    fetch('/salvar-operacao/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken() // Token CSRF obrigatório para segurança no Django
        },
        body: JSON.stringify({ operacao, resultado }) // Envia operação e resultado como JSON
    });
}

// Função que recupera o valor do token CSRF armazenado nos cookies
function getCSRFToken() {
    return document.cookie.split('; ')
        .find(row => row.startsWith('csrftoken')) // Busca o cookie chamado 'csrftoken'
        ?.split('=')[1]; // Retorna apenas o valor do token
}
