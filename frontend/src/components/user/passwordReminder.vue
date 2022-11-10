<template>
    <div class="login-container">
      <h1 class="title">Przypomnienie hasła</h1>
  
      <br>

      <b-field label="Podaj emaila/jeden z emaili">
        <b-input type="email"
            maxlength="30"
            required>
        </b-input>
      </b-field>

      <b-button type="is-primary" expanded>RESETUJ HASŁO</b-button>
    </div>
</template>
  
<script>
export default {
name: "passwordReminder",
};
</script>

<style>
.login-container {
    margin: 0 auto;
    max-width: 320px;
}
  
.title {
    text-align: center;
}
</style>