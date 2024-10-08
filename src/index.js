// Fonction pour récupérer les données du fichier JSON
async function fetchData() {
    const response = await fetch('articles.json'); // Remplacez 'data.json' par le nom de votre fichier JSON
    const data = await response.json();
    return data;
}

// Fonction pour afficher les articles
function displayArticles(articles) {
    const articleList = document.getElementById('article-list');

    articles.reverse().forEach(article => {
        if (article.metadata.visibility != "public") return;
        const card = document.createElement('div');
        card.classList.add('col');
        card.innerHTML = `
            <div class="card h-100" onclick="window.location.href='${article.html_path}'">
                <img src="${article.image_path}" class="card-img-top img_ratio_fixed" alt="${article.metadata.title}">
                <div class="card-body">
                    <h5 class="card-title">${article.metadata.title}</h5>
                    <p class="card-text">Par ${article.metadata.author} - ${article.metadata.date}</p>
                    <a href="${article.html_path}" class="btn btn-primary">Lire l'article</a>
                </div>
            </div>
        `;
        articleList.appendChild(card);
    });
}

function displayCategories(categories) {
    const categoriesList = document.getElementById('categories-list');

    categories.forEach(category => {
        const listItem = document.createElement('li');
        listItem.textContent = category;
        categoriesList.appendChild(listItem);
    });
}

// Charger et afficher les catégories
//fetchData().then(data => displayCategories(data.categories));

// Charger et afficher les articles
fetchData().then(data => displayArticles(data));


