// Query the Category in the Blog
let category = document.getElementById("category");

// Wait the clic to display Blog by Category
document.addEventListener('click', (event) => {
    const categoryElement = event.target.closest('.category');

    if (!categoryElement) return;

    event.preventDefault();

    const category = categoryElement.dataset.category;

    fetch(`/blog/blogs/${category}/`)
        .then(response => response.json())
        .then(data => {
            const blogs = document.getElementById("blog");

            blogs.innerHTML = "";
            
            if (data.blogs.length > 0) {
                data.blogs.forEach(blog => {
                    blogs.innerHTML += `
                        <article class="blog">
                            <h3 class="blog-name"> ${ blog.name } </h3>
                            <p> ${ blog.preview } </p>
                            <p> Categoria: ${ blog.category } </p>
                            <p> Fecha de Creacion: ${ blog.created_at } </p>
                            <a href="/blog/detail/${blog.id}/" class="detail-blog"> VER MAS </a>
                        </article>
                    `;
                });
            // If the category don't exist in the Blog show a message
            } else {
                blogs.innerHTML = `<p> ${data.message} </p>`;
            }
        })
        .catch(error => console.error("Error:", error));
});