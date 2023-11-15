<!DOCTYPE html>
<html>
    <body>

        <h2>Relatório dos dados enviados</h2>

            <?php
                if ($_SERVER["REQUEST_METHOD"] == "POST") {
                    echo "<b>Nome Completo:</b> " . $_POST["nome"] . "<br>";
                    echo "<b>CPF:</b> " . $_POST["cpf"] . "<br>";
                    echo "<b>Data de nascimento:</b> " . $_POST["data_nascimento"] . "<br>";
                    echo "<b>Sexo:</b> " . $_POST["sexo"] . "<br>";
                    echo "<b>Estado Civil:</b> " . $_POST["estcivil"] . "<br>";
                    echo "<b>E-mail:</b> " . $_POST["email"] . "<br>";
                    echo "<b>Website:</b> " . $_POST["website"] . "<br>";
                    echo "<b>Endereço:</b> " . $_POST["endereco"] . "<br>";
                    echo "<b>Bairro:</b> " . $_POST["bairro"] . "<br>";
                    echo "<b>Cidade:</b> " . $_POST["cidade"] . "<br>";
                    echo "<b>CEP:</b> " . $_POST["cep"] . "<br>";
                    echo "<b>UF:</b> " . $_POST["uf"] . "<br>";
                    echo "<b>Telefone:</b> " . $_POST["telefone"] . "<br>";
                    echo "<b>Celular:</b> " . $_POST["celular"] . "<br>";
                    echo "<b>Usuário:</b> " . $_POST["login"] . "<br>";

                    echo "<b>Informações que o usuário deseja receber:</b> ";
                    $interesses = array();
                    if (isset($_POST['interesse1'])) {
                        $interesses[] = "Cultura";
                    }
                    if (isset($_POST['interesse2'])) {
                        $interesses[] = "Economia";
                    }
                    if (isset($_POST['interesse3'])) {
                        $interesses[] = "Esportes";
                    }
                    if (isset($_POST['interesse4'])) {
                        $interesses[] = "Educação";
                    }
                    if (isset($_POST['interesse5'])) {
                        $interesses[] = "Culinária";
                    }
                    if (isset($_POST['interesse6'])) {
                        $interesses[] = "Empregos";
                    }
                    if (isset($_POST['interesse7'])) {
                        $interesses[] = "Política";
                    }
                    if (isset($_POST['interesse8'])) {
                        $interesses[] = "Moda e Estilo";
                    }
                    $interesses_string = implode(", ", $interesses);
                    echo $interesses_string;
                    
                }

            ?>

    </body>
</html>
