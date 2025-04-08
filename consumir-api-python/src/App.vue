<script>
export default {
  data() {
      return {
        dado: 'Tupla na tabela Rol',
        valor: "Termo tal",
        tuplas: [["procedimento 1", "nan", "2025"], ["procedimento 2", "nan", "2025"], ["procedimento 3", "nan", "2025"]]
      };
  },
  methods: {
    async buscarNaApi() {
      const response = await fetch("http://127.0.0.1:5000/procedimentos")
      const procedimentos = await response.json()
      // const procedimentoBuscado = Object.values(procedimentos).find((p) => p === this.valor)

      console.log(Object.values(procedimentos))
    }
  }
}
</script>

<template>
  <header>
    <h1>Consultar Tabela Rol de Procedimentos</h1>

  </header>

  <main>
    <label for="buscar-termo">
      <input type="text" name="buscar-termo" id="search-input" placeholder="Buscar por termo na tabela..." v-model="valor">
    </label>
    <button id="search-button" v-on:click="buscarNaApi">Buscar</button> 
  </main>
  <tr>
    <th>Procedimento</th>
    <th>RN(alteração)</th>
    <th>Vigência</th>
  </tr>
  <tr v-for="tupla in tuplas" :id="'tp-' + tuplas.indexOf(tupla)">
    <td v-for="item in tupla" :id="'tp-' + tuplas.indexOf(tupla) + '-it-' + tupla.indexOf(item)"> 
      {{ item }} 
    </td>
  </tr>
  
</template>


