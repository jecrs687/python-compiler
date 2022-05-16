
        .class public trabCompiladores
        .super java/lang/Object
        
.method public static main([Ljava/lang/String;)V
.limit stack 50
.limit locals 50
        ldc 2
        ldc 2
        iadd
        istore 0

        getstatic java/lang/System/out Ljava/io/PrintStream;
        iload 0
        invokevirtual java/io/PrintStream/println(I)V
        
        getstatic java/lang/System/out Ljava/io/PrintStream;
        ldc 2
        ldc 2
        iadd
        ldc 2
        iadd
        ldc 2
        ldc 2
        imul
        ldc 2
        imul
        ldc 2
        imul
        iadd
        invokevirtual java/io/PrintStream/println(I)V
    
    return
    .end method