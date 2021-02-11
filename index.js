function mainButton(id)
{
    eel.buttonPressed(id, path)
}

function changeButtonContent(id, content)
{
    document.getElementById(id.toString()).innerHTML = content
}

eel.expose(changePath)
function changePath(newPath)
{
    path = newPath
    for(a = 0; a < 12; a++)
    {
        console.log(path + a)
        changeButtonContent(a, ("<img src='" + path + a + ".png" + "'>"))
    }
}

changePath("./files/")