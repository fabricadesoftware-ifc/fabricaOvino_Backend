<template>
  <div class="tile is-parent">
    <div class="tile is-child is-3">
      <strong>Permissões</strong>
    </div>
    <div class="tile is-child is-9 permissions">
      <div class="select-perms">
        <b-field>
          <b-select multiple size="10" native-size="10" v-model="selectPermissionsFrom">
            <option
              v-for="permission in permissions_from"
              :key="permission.id"
              :value="permission.id"
            >{{permission.name}}</option>
          </b-select>
        </b-field>
        <b-button
          type="is-info"
          @click="selectAllPerm"
          icon-right="arrow-right-bold-outline"
        >Escolher todos</b-button>
      </div>
      <div class="select-buttons">
        <b-button type="is-info" @click="selectPerm" icon-right="arrow-right-bold-outline"></b-button>
        <b-button type="is-info" @click="removePerm" icon-right="arrow-left-bold-outline"></b-button>
      </div>
      <div class="select-perms">
        <b-field>
          <b-select multiple native-size="10" v-model="selectPermissionsTo">
            <option
              v-for="permission in choosed_permissions"
              :key="permission.id"
              :value="permission.id"
            >{{permission.name}}</option>
          </b-select>
        </b-field>
        <b-button
          type="is-info"
          @click="removeAllPerm"
          icon-right="arrow-left-bold-outline"
        >Remover todos</b-button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    choosedIds: Array,
    edit: {
      type: Boolean,
      default () {
        return false
      }
    }
  },
  data () {
    return {
      selectPermissionsFrom: [],
      selectPermissionsTo: [],
      permissions: [],
    }
  },
  async fetch() {
    this.permissions = await this.$axios.$get("/api/v1/permissions/");
  },
  computed: {
    permissions_from() {
      let choosed = this.choosedIds

      var perms = this.permissions.filter(function(permission) {
        return (choosed.includes(permission.id) == false)
      })
      return perms
    },
    choosed_permissions() {
      let choosed = this.choosedIds
      var perms = this.permissions.filter(function(permission) {
        return choosed.includes(permission.id)
      });
      return perms;
    }
  },
  methods: {
    selectPerm() {
      this.choosedIds = [ ...this.choosedIds, ...this.selectPermissionsFrom]
      this.selectPermissionsFrom = []
      this.$emit("update-choosed", this.choosedIds)
    },
    selectAllPerm() {
      this.choosedIds = [ ...this.choosedIds, ...this.permissions_from.map( ({id}) => id)]
      this.selectPermissionsFrom = []
      this.$emit("update-choosed", this.choosedIds)
    },
    removePerm() {
      this.choosedIds = this.choosedIds.filter( (id) => !this.selectPermissionsTo.includes(id))
      this.selectPermissionsTo = []
      this.$emit("update-choosed", this.choosedIds)
    },
    removeAllPerm() {
      this.choosedIds = []
      this.selectPermissionsTo = []
      this.$emit("update-choosed", this.choosedIds)
    },
  }
}
</script>

<style>
.permissions {
  display: flex;
  height: 400px;
}
.select-perms {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 40%;
}

.select-buttons {
  display: flex;
  flex-direction: column;
  padding: 10px;
  margin-top: 100px;
}

.select-buttons button {
  margin-bottom: 10px;
}
</style>
