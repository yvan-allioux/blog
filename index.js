let articles = [];

// Fonction pour récupérer les données du fichier JSON
async function fetchData() {
    const response = await fetch('articles.json');
    articles = await response.json();
    return articles;
}

// Fonction pour afficher les articles
function displayArticles(filteredArticles) {
    const articleList = document.getElementById('article-list');
    articleList.innerHTML = '';

    filteredArticles.forEach(article => {
        const card = document.createElement('div');
        card.classList.add('col');
        card.innerHTML = `
                    <div class="card h-100">
                        <img src="${article.image_path}" class="card-img-top" alt="${article.metadata.title}">
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

// Fonction pour trier les articles par date
function sortByDate() {
    const sortedArticles = [...articles].sort((a, b) => new Date(b.metadata.date) - new Date(a.metadata.date));
    displayArticles(sortedArticles);
}

// Fonction pour trier les articles par catégorie
function sortByCategory(category) {
    const filteredArticles = articles.filter(article => article.metadata.categories.includes(category));
    displayArticles(filteredArticles);
}

// Fonction pour trier les articles par tag
function sortByTag(tag) {
    const filteredArticles = articles.filter(article => article.metadata.tags.includes(tag));
    displayArticles(filteredArticles);
}

// Charger et afficher les articles
fetchData().then(data => {
    displayArticles(data);

    // Remplir les listes déroulantes des catégories et des tags
    const categoryDropdown = document.getElementById('sortByCategory');
    const tagDropdown = document.getElementById('sortByTag');
    const categories = new Set(data.flatMap(article => article.metadata.categories));
    const tags = new Set(data.flatMap(article => article.metadata.tags));

    categories.forEach(category => {
        const listItem = document.createElement('li');
        const link = document.createElement('a');
        link.classList.add('dropdown-item');
        link.href = '#';
        link.textContent = category;
        link.addEventListener('click', () => {
            sortByCategory(category);
        });
        listItem.appendChild(link);
        categoryDropdown.nextElementSibling.appendChild(listItem);
    });

    tags.forEach(tag => {
        const listItem = document.createElement('li');
        const link = document.createElement('a');
        link.classList.add('dropdown-item');
        link.href = '#';
        link.textContent = tag;
        link.addEventListener('click', () => {
            sortByTag(tag);
        });
        listItem.appendChild(link);
        tagDropdown.nextElementSibling.appendChild(listItem);
    });

    // Ajouter l'événement pour trier par date
    document.getElementById('sortByDate').addEventListener('click', sortByDate);
});