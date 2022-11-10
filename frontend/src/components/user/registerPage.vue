<template>
  <div class="register-container">
    <h1 class="title">Rejestracja</h1>
  
    <br>

    <b-field label="Imię">
        <b-input maxlength="30"
            required>
        </b-input>
    </b-field>

    <b-field label="Nazwisko">
        <b-input maxlength="30"
            required>
        </b-input>
    </b-field>

    <b-field label="Email">
        <b-input type="email"
            maxlength="30"
            required>
        </b-input>
    </b-field>

    <b-field label="Login">
        <b-input maxlength="30"
            required>
        </b-input>
    </b-field>

    <b-field label="Hasło">
        <b-input type="password"
            password-reveal
            minlength="8"
            maxlength="30"
            required>
        </b-input>
    </b-field>

    <b-field label="Powtórz hasło">
        <b-input type="password"
            password-reveal
            minlength="8"
            maxlength="30"
            required>
        </b-input>
    </b-field>

    <br>

    <b-button type="is-primary" :to="{ name: 'login' }" tag="router-link" expanded>
      ZAŁÓŻ KONTO
    </b-button>

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
  max-width: 320px;
}

.title {
  text-align: center;
}

.p-login {
  text-decoration: underline;
}

</style>