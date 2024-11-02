// fireworks.js
window.onload = function() {
    var canvas = document.getElementById('canvas');
    var ctx = canvas.getContext('2d');

    // 设置画布大小为视窗大小
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    var fireworks = [];
    var particles = [];

    function Firework(sx, sy, tx, ty) {
        this.x = sx;
        this.y = sy;
        this.sx = sx;
        this.sy = sy;
        this.tx = tx;
        this.ty = ty;
        this.distanceToTarget = calculateDistance(sx, sy, tx, ty);
        this.distanceTraveled = 0;
        this.segment = document.createElement('canvas');
        var segmentContext = this.segment.getContext('2d');
        this.segment.width = 2;
        this.segment.height = 20;
        segmentContext.fillStyle = 'rgba(170, 170, 170, 0.8)';
        segmentContext.beginPath();
        segmentContext.arc(1, 10, 1, 0, Math.PI * 2, true);
        segmentContext.fill();
    }

    Firework.prototype.update = function(index) {
        var vx = (this.tx - this.sx) / this.distanceToTarget;
        var vy = (this.ty - this.sy) / this.distanceToTarget;
        this.distanceTraveled += Math.sqrt(vx * vx + vy * vy);
        this.x += vx;
        this.y += vy;
        if(this.distanceTraveled >= this.distanceToTarget) {
            explodeFireworks(index);
        }
    };

    function Particle(x, y, radius, color) {
        this.x = x;
        this.y = y;
        this.radius = radius;
        this.color = color;
        this.velocity = {
            x: (Math.random() - 0.5) * 10,
            y: (Math.random() - 0.5) * 10
        };
    }

    Particle.prototype.draw = function() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);
        ctx.fillStyle = this.color;
        ctx.fill();
    };

    Particle.prototype.update = function() {
        this.x += this.velocity.x;
        this.y += this.velocity.y;
        if(this.radius > 0.2) {
            this.radius -= 0.1;
        }
    };

    function explodeFireworks(index) {
        for(var i = 0; i < 30; i++) {
            var p = new Particle(fireworks[index].x, fireworks[index].y, Math.random() * 2 + 2, 'rgb(' + Math.floor(Math.random()*255) + ',' + Math.floor(Math.random()*255) + ',' + Math.floor(Math.random()*255) + ')');
            particles.push(p);
        }
        fireworks.splice(index, 1);
    }

    function animate() {
        requestAnimationFrame(animate);
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        for(var i = 0; i < fireworks.length; i++) {
            fireworks[i].update(i);
        }
        for(var i = 0; i < particles.length; i++) {
            particles[i].draw();
            particles[i].update();
        }
        particles = particles.filter(function(particle) { return particle.radius > 0; });
    }

    animate();

    function calculateDistance(x1, y1, x2, y2) {
        return Math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
    }
};