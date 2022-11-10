<!-- <template>
  <div>Rejestracja
    <p>Imię</p>
    <input v-model="name" placeholder="Jan">
    <p>Nazwisko</p>
    <input v-model="surname" placeholder="Kowalski">
    <p>Email</p>
    <input v-model="email" placeholder="e@e.com">
    <p>Login</p>
    <input v-model="login" placeholder="user1">
    <p>Hasło</p>
    <input v-model="password" placeholder="pass#12">
    <p>Powtórz hasło</p>
    <input v-model="repeatedPassword" placeholder="pass#12">
    <br><br>
    <button>ZAŁÓŻ KONTO</button>
  </div>
  
</template> -->

<template>
  <div class="register-container">
    <h1 class="title">Rejestracja</h1>
  
    <br>

    <b-field label="Imię">
        <b-input maxlength="30"></b-input>
    </b-field>

    <b-field label="Nazwisko">
        <b-input maxlength="30"></b-input>
    </b-field>

    <b-field label="Email">
        <b-input type="email"
            maxlength="30">
        </b-input>
    </b-field>

    <b-field label="Login">
        <b-input maxlength="30">
        </b-input>
    </b-field>

    <b-field label="Hasło">
        <b-input type="password"
            password-reveal
            minlength="8"
            maxlength="30">
        </b-input>
    </b-field>

    <b-field label="Powtórz hasło">
        <b-input type="password"
            password-reveal
            minlength="8"
            maxlength="30">
        </b-input>
    </b-field>

    <br>

    <b-button type="is-primary" expanded>ZAŁÓŻ KONTO</b-button>

    <br>
    <br>

    <b-navbar-item :to="{ name: 'login' }" tag="router-link">
        Masz już konto? &nbsp;<p class="p-login"> Zaloguj się. </p>
    </b-navbar-item>

  </div>
</template>

<script>
export default {
  name: "registerPage",
};
</script>

<style>
.register-container {
  margin: 0 auto;
  max-width: 300px;
}

.title {
  text-align: center;
}

.p-login {
  text-decoration: underline;
}

</style>