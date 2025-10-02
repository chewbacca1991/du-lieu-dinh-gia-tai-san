import React from 'react';

function App() {
    const handleSubmit = async (e) => {
        e.preventDefault();
        const data = new FormData(e.target);
        const response = await fetch('/predict', {
            method: 'POST',
            body: JSON.stringify(Object.fromEntries(data)),
            headers: {
                'Content-Type': 'application/json',
            },
        });
        const result = await response.json();
        console.log(result);
    };

    return (
        <div>
            <h1>Dự đoán Giá Trị Tài Sản Bất Động Sản</h1>
            <form onSubmit={handleSubmit}>
                <input name="location" placeholder="Vị trí" required />
                <input name="area" type="number" placeholder="Diện tích" required />
                <input name="rooms" type="number" placeholder="Số phòng" required />
                <input name="date_sold" type="date" required />
                <button type="submit">Dự đoán</button>
            </form>
        </div>
    );
}

export default App;
