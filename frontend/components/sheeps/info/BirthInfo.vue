<template>
  <section>
    <section class="section is-main-section">
      <div style="text-align: right">
        <router-link :to="localePath({ name: 'sheep' })" class="button">
          Voltar
        </router-link>
        <router-link :to="localePath({ name: 'birth' })" class="button">
          Novo Parto
        </router-link>
        <router-link to="/" class="button"> Dashboard </router-link>
      </div>
      <card-component
        title="Histórico de Partos"
        icon="file-document-multiple-outline"
        class="has-table has-mobile-sort-spaced"
      >
        <b-table
          striped
          :data="value.births"
          paginated
          paginate-position="bottom"
          aria-next-label="Next page"
          aria-previous-label="Previous page"
          aria-page-label="Page"
          aria-current-label="Current page"
          per-page="10"
        >
          <template v-slot="props">
            <b-table-column
              v-for="(column, index) in columns"
              :key="index"
              :field="column.field"
              :label="column.label"
              :sortable="column.sortable"
            >
              <span v-if="column.field == 'date'">
                {{ new Date(props.row[column.field]).toLocaleDateString() }} -
                {{ new Date(props.row[column.field]).toLocaleTimeString() }}
              </span>

              <span v-else>
                {{ props.row[column.field] }}
              </span>
            </b-table-column>
            <b-table-colunm
              custom-key="actions"
              class="is-actions-cell"
              label="Ações"
            >
              <b-button
                type="is-small is-primary"
                icon-left="pencil"
                @click="editBirth(props.row)"
              ></b-button>
              <b-button
                type="is-small is-danger"
                icon-left="trash-can-outline"
                @click="confirmRemove(props.row)"
              ></b-button>
            </b-table-colunm>
          </template>
        </b-table>
      </card-component>
    </section>
  </section>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import CardComponent from '@/components/templates/CardComponent.vue'
export default {
  components: { CardComponent },
  props: {
    value: {
      type: Object,
      default() {
        return {}
      }
    }
  },
  data() {
    return {
      columns: [
        {
          field: 'id',
          label: 'Nº Parto',
          sortable: true
        },
        {
          field: 'date',
          label: 'Data e Hora',
          sortable: true
        },
        {
          field: 'newborns_quantity',
          label: 'Quantidade de filhotes',
          sortable: true
        },
        {
          field: 'observations',
          label: 'Observações',
          sortable: true
        }
      ],
      sheep: {}
    }
  },
  computed: {
    ...mapState('birth', ['births'])
  },
  created() {
    this.getBirths()
  },
  methods: {
    ...mapActions('birth', ['getBirths']),
    editBirth(birth) {
      this.$router.push({
        name: `sheeps-editBirth___${this.$i18n.locale}`,
        params: { birth }
      })
    },
    confirmRemove(birth) {
      this.$buefy.dialog.confirm({
        title: 'Excluir parto?',
        message: 'Você tem certeza que deseja excluir este item?',
        confirmText: 'Excluir',
        cancelText: 'Cancelar',
        type: 'is-danger',
        hasIcon: true,
        onConfirm: () => this.remove(birth)
      })
    }
  }
}
</script>

<style></style>
