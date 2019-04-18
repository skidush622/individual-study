camel-hazelcast
===============

Example usage of Hazelcast for Camel AggregationRepository &amp; Camel Quartz (to use the distributed timer ability)

## Hazelcast as a repository for distributed aggregators

You can use Hazelcast to aggregate events using multiple nodes. Just add it to your Spring configuration like so:

```xml
    <hz:hazelcast id="hazelcastInstance">
        <hz:config>
        <!-- ... Hazelcast config ... -->
        </hz:config>
    </hz:hazelcast>
    <bean id="hazelcastAggregatorRepository" class="me.smecsia.common.camel.HazelcastAggregationRepository">
        <property name="hazelcastInstance" ref="hazelcastInstance"/>
        <property name="repository" value="repositoryName"/>
    </bean>
    
    <!-- ... --->
    
    <!-- And just add this repository to "aggregate": -->
    <aggregate strategyRef="aggregatorStrategy" aggregationRepositoryRef="hazelcastAggregatorRepository">
    </aggregate>

```

## Distributed timer with Hazelcast

You can use Hazelcast to provide the distributed lock to start the camel-quartz on a particular node only. 
Add the following configuration to your Spring config:

```xml
    <bean id="quartz" class="org.apache.camel.component.quartz.QuartzComponent">
        <property name="autoStartScheduler" value="false"/>
    </bean>
    <bean class="me.smecsia.common.camel.HazelcastQuartzSchedulerStartupListener">
        <property name="hazelcastInstance" ref="hazelcastInstance"/>
        <property name="quartzComponent" ref="quartz"/>
    </bean>
```

And now you can use camel-quartz just like it is adviced in the [official docs](http://camel.apache.org/quartz.html)
