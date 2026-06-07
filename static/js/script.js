console.log("Student Management System Loaded");

// Delete confirmation

function confirmDelete(){

    return confirm(
        "Are you sure you want to delete this student?"
    );

}
function toggleDarkMode(){

    document.body.classList.toggle(
        "dark-mode"
    );

    localStorage.setItem(
        "darkMode",
        document.body.classList.contains(
            "dark-mode"
        )
    );
}

window.onload = function(){

    if(
        localStorage.getItem(
            "darkMode"
        ) === "true"
    ){

        document.body.classList.add(
            "dark-mode"
        );
    }
}