/** @odoo-module **/    

import { registry } from '@web/core/registry';
const { Component, useState, onWillStart, useRef } = owl;
import { useService } from "@web/core/utils/hooks";

class productionsPayment extends Component {
    setup() {
        this.state = useState({
            task:{name:""},
            productionList:[],
            isEdit: false,
            activeId: false,
        })
        this.orm = useService("orm")
        this.model = "upocafe.payment"
        this.searchInput = useRef("search-input")

        onWillStart(async ()=>{
            await this.getAllProductions()
        })
    }

    async getAllProductions(){
        this.state.taskList = await this.orm.searchRead(this.model, [], ["name"])
    }

    addProduction(){
        this.resetForm()
        this.state.activeId = false
        this.state.isEdit = false
    }

    editProduction(task){
        this.state.activeId = task.id
        this.state.isEdit = true
        this.state.task = {...task}
    }

    async saveProduction(){

        if (!this.state.isEdit){
            await this.orm.create(this.model, [this.state.task])
            this.resetForm()
        } else {
            await this.orm.write(this.model, [this.state.activeId], this.state.task)
        }
        $('#exampleModal').modal('hide')
        this.resetForm()
        await this.getAllTasks()
    }

    resetForm(){
        this.state.task = {name:""}
    }

    async deleteProductions(production){
        await this.orm.unlink(this.model, [production.id])
        await this.getAllTasks()
    }

    async searchProductions(){
        const text = this.searchInput.el.value
        this.state.taskList = await this.orm.searchRead(this.model, [['name','ilike',text]], ["name"])
    }

    async updateCapacity(e, production){
        await this.orm.write(this.model, [production.id], {capacity: e.target.value})
        await this.getAllTasks()
    }    
}
    
productionsPayment.template = 'owl.productionsPayment';
registry.category('actions').add('owl.action_productionsPayment_js', productionsPayment);