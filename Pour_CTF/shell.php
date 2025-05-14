<?php
echo '<pre>';
echo '✅ EXECUTION OK
';
echo 'Fichiers dans ce dossier:
';
print_r(scandir('.'));
echo '
Contenu index.php:
';
@readfile('index.php');
echo '</pre>';
?>
