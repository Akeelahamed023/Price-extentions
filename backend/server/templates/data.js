fetch('http://127.0.0.1:8000/api/all/')
  .then(response => response.json())
  .then(data => {
    const tableBody = document.querySelector('#price-table tbody');

    data.forEach(item => {
      const row = document.createElement('tr');

      const categoryCell = document.createElement('td');
      categoryCell.textContent = item.Category.CategoryChoices;
      row.appendChild(categoryCell);

      const brandCell = document.createElement('td');
      brandCell.textContent = item.brand.BrandChoices;
      row.appendChild(brandCell);

      const modelCell = document.createElement('td');
      modelCell.textContent = item.model.ModelChoices;
      row.appendChild(modelCell);

      const priceCell = document.createElement('td');
      priceCell.textContent = item.price;
      row.appendChild(priceCell);

      const linkCell = document.createElement('td');
      linkCell.textContent = item.link;
      row.appendChild(linkCell);

      tableBody.appendChild(row);
    });

    // Populate the filters
    const filters = document.getElementsByClassName('table-filter');
    Array.from(filters).forEach(filter => {
      const colIndex = filter.parentElement.getAttribute('col-index');
      const values = new Set(data.map(item => item[colIndex]));
      values.forEach(value => {
        const option = document.createElement('option');
        option.textContent = value;
        filter.appendChild(option);
      });
    });
  })
  .catch(error => {
    console.error('Error:', error);
  });