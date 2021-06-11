<<head>
?title? welcome to Node red dashboard./title><h3>Testing dynamic scripts with Dashboard </title>
<</head>
<
<body>
<h3>Testing dynamic scripts with Dashboard 2.0</h3>

{{msg.payload}}
<script>
    (function(scope) {
        console.log('Position 1');
        console.dir(scope);
        scope.$watch('msg.payload', function(data) {
            console.log('Position 2');
            console.dir(data);
        });
    })(scope);
</script>

</body>
</html>