<template>
  <div class="login-container">
    <h1 class="title">Logowanie</h1>

    <br>

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

    <b-navbar-item :to="{ name: 'passwordReminder' }" tag="router-link">
        Nie pamiętam hasła.
    </b-navbar-item>

    <br>
    <br>

    <b-button type="is-primary" expanded>ZALOGUJ SIĘ</b-button>

    <br>
    <br>

    <b-navbar-item :to="{ name: 'register' }" tag="router-link">
        Nie masz konta? &nbsp;<p class="p-register"> Zarejestruj się. </p>
    </b-navbar-item>

  </div>
</template>

<script>
export default {
  name: "loginPage",
};
</script>

<style>
.login-container {
  margin: 0 auto;
  max-width: 300px;
}

.title {
  text-align: center;
}

.p-register {
  text-decoration: underline;
}

</style>