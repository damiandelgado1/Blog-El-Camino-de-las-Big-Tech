// Query the Category in the Blog
let category = document.getElementsByClassName("category");

// Wait the clic to display Blog by Category
document.addEventListener('click', (event) => {
    const categoryElement = event.target.closest('.category');

    if (!categoryElement) return;

    event.preventDefault();

    const category = event.target.dataset.category;

    fetch(`/blog/blogs/${category}/`)
        .then(response => response.json())
        .then(data => {
            if (data.blogs.length > 0) {
                const blogs = document.getElementByClassName("blogs");

                blogs.innerHTML = "";

                // If category exist in the Blog show them
                if (data.blogs.length > 0) {
                    data.blogs.forEach(blog => {
                        blog.innerHTML += `
                            <article class="blog">
                                <h3> ${blog.name} </h3>
                                <p> ${blog.preview} </p>
                            </article>
                        `;
                    });
                }
            // If the category don't exist in the Blog show a message
            } else {
                blog.innerHTML = `<p> ${data.message} </p>`;
            }
        })
        .catch(error => console.error("Error:", error));
});