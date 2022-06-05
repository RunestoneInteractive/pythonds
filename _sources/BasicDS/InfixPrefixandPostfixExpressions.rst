..  Copyright (C)  Brad Miller, David Ranum
    This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.


Infix, Prefix, and Postfix Expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you write an arithmetic expression such as B · C, the form of the
expression provides you with information so that you can interpret it
correctly. In this case we know that the variable B is being multiplied
by the variable C since the multiplication operator · appears between
them in the expression. This type of notation is referred to as
**infix** since the operator is *in between* the two operands that it is
working on.

Consider another infix example, A + B · C. The operators + and · still
appear between the operands, but there is a problem. Which operands do
they work on? Does the + work on A and B, or does the · take B and C?
The expression seems ambiguous.

In fact, you have been reading and writing these types of expressions
for a long time and they do not cause you any problem. The reason for
this is that you know something about the operators + and ·. Each
operator has a **precedence** level. Operators of higher precedence are
used before operators of lower precedence. The only thing that can
change that order is the presence of parentheses. The precedence order
for arithmetic operators places multiplication and division above
addition and subtraction. If two operators of equal precedence appear,
then a left-to-right ordering or associativity is used.

Let’s interpret the troublesome expression A + B · C using operator
precedence. B and C are multiplied first, and A is then added to that
result. (A + B) · C would force the addition of A and B to be done
first before the multiplication. In the expression A + B + C, by precedence
(via associativity), the leftmost + would be done first.

Although all this may be obvious to you, remember that computers need to
know exactly what operations to perform and in what order. One way to
write an expression that guarantees there will be no confusion with
respect to the order of operations is to create what is called a **fully
parenthesized** expression. This type of expression uses one pair of
parentheses for each operator. The parentheses dictate the order of
operations; there is no ambiguity. There is also no need to remember any
precedence rules.

The expression A + B · C + D can be rewritten as ((A + (B · C)) + D)
to show that the multiplication happens first, followed by the leftmost
addition. A + B + C + D can be written as (((A + B) + C) + D) since the
addition operations associate from left to right.

There are two other very important expression formats that may not seem
obvious to you at first. Consider the infix expression A + B. What would
happen if we moved the operator before the two operands? The resulting
expression would be + A B. Likewise, we could move the operator to the
end, resulting in A B +. These look a bit strange.

These changes to the position of the operator with respect to the
operands create two new expression formats, **prefix** and **postfix**.
Prefix expression notation requires that all operators precede the two
operands that they work on. Postfix, on the other hand, requires that
its operators come after the corresponding operands. A few more examples
should help to make this a bit clearer (see :ref:`Table 2 <tbl_example1>`).

A + B · C would be written as + A · B C in prefix. The multiplication
operator comes immediately before the operands B and C, denoting that ·
has precedence over +. The addition operator then appears before the A
and the result of the multiplication.

In postfix, the expression would be A B C · +. Again, the order of
operations is preserved since the · appears immediately after the B and
the C, denoting that · has precedence, with + coming after. Although
the operators moved and now appear either before or after their
respective operands, the order of the operands stayed exactly the same
relative to one another.

.. _tbl_example1:

.. table:: **Table 2: Examples of Infix, Prefix, and Postfix Expressions**

    ============================ ======================= ========================
            **Infix Expression**   **Prefix Expression**   **Postfix Expression**
    ============================ ======================= ========================
                           A + B                  \+ A B                    A B +
                       A + B · C              \+ A · B C                A B C · +
    ============================ ======================= ========================


Now consider the infix expression (A + B) · C. Recall that in this
case, infix requires the parentheses to force the performance of the
addition before the multiplication. However, when A + B was written in
prefix, the addition operator was simply moved before the operands, + A
B. The result of this operation becomes the first operand for the
multiplication. The multiplication operator is moved in front of the
entire expression, giving us · + A B C. Likewise, in postfix A B +
forces the addition to happen first. The multiplication can be done to
that result and the remaining operand C. The proper postfix expression
is then A B + C ·.

Consider these three expressions again (see :ref:`Table 3 <tbl_parexample>`).
Something very important has happened. Where did the parentheses go? Why
don’t we need them in prefix and postfix? The answer is that the
operators are no longer ambiguous with respect to the operands that they
work on. Only infix notation requires the additional symbols. The order
of operations within prefix and postfix expressions is completely
determined by the position of the operator and nothing else. In many
ways, this makes infix the least desirable notation to use.

.. _tbl_parexample:

.. table:: **Table 3: Comparison of Infix, Prefix, and Postfix Expressions**

    ============================ ======================= ========================
            **Infix Expression**   **Prefix Expression**   **Postfix Expression**
    ============================ ======================= ========================
                     (A + B) · C               · + A B C                A B + C ·
    ============================ ======================= ========================


:ref:`Table 4 <tbl_example3>` shows some additional examples of infix expressions and
the equivalent prefix and postfix expressions. Be sure that you
understand how they are equivalent in terms of the order of the
operations being performed.

.. _tbl_example3:

.. table:: **Table 4: Additional Examples of Infix, Prefix, and Postfix Expressions**

    ============================ ======================= ========================
            **Infix Expression**   **Prefix Expression**   **Postfix Expression**
    ============================ ======================= ========================
                   A + B · C + D         \+ \+ A · B C D            A B C · + D +
               (A + B) · (C + D)           · + A B + C D            A B + C D + ·
                   A · B + C · D          \+ · A B · C D            A B · C D · +
                   A + B + C + D          \+ + + A B C D            A B + C + D +
    ============================ ======================= ========================


Conversion of Infix Expressions to Prefix and Postfix
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

So far, we have used ad hoc methods to convert between infix expressions
and the equivalent prefix and postfix expression notations. As you might
expect, there are algorithmic ways to perform the conversion that allow
any expression of any complexity to be correctly transformed.

The first technique that we will consider uses the notion of a fully
parenthesized expression that was discussed earlier. Recall that A + B
· C can be written as (A + (B · C)) to show explicitly that the
multiplication has precedence over the addition. On closer observation,
however, you can see that each parenthesis pair also denotes the
beginning and the end of an operand pair with the corresponding operator
in the middle.

Look at the right parenthesis in the subexpression (B · C) above. If we
were to move the multiplication symbol to that position and remove the
matching left parenthesis, giving us B C ·, we would in effect have
converted the subexpression to postfix notation. If the addition
operator were also moved to its corresponding right parenthesis position
and the matching left parenthesis were removed, the complete postfix
expression would result (see :ref:`Figure 6 <fig_moveright>`).

.. _fig_moveright:

.. figure:: Figures/moveright.png
   :align: center

   Figure 6: Moving Operators to the Right for Postfix Notation

If we do the same thing but instead of moving the symbol to the position
of the right parenthesis, we move it to the left, we get prefix notation
(see :ref:`Figure 7 <fig_moveleft>`). The position of the parenthesis pair is
actually a clue to the final position of the enclosed operator.

.. _fig_moveleft:

.. figure:: Figures/moveleft.png
   :align: center

   Figure 7: Moving Operators to the Left for Prefix Notation


So in order to convert an expression, no matter how complex, to either
prefix or postfix notation, fully parenthesize the expression using the
order of operations. Then move the enclosed operator to the position of
either the left or the right parenthesis depending on whether you want
prefix or postfix notation.

Here is a more complex expression: (A + B) · C - (D - E) · (F + G).
:ref:`Figure 8 <fig_complexmove>` shows the conversion to prefix and postfix
notations.

.. _fig_complexmove:

.. figure:: Figures/complexmove.png
   :align: center

   Figure 8: Converting a Complex Expression to Prefix and Postfix Notations

General Infix-to-Postfix Conversion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We need to develop an algorithm to convert any infix expression to a
postfix expression. To do this we will look closer at the conversion
process.

Consider once again the expression A + B · C. As shown above,
A B C · + is the postfix equivalent. We have already noted that the
operands A, B, and C stay in their relative positions. It is only the
operators that change position. Let’s look again at the operators in the
infix expression. The first operator that appears from left to right is
+. However, in the postfix expression, + is at the end since the next
operator, ·, has precedence over addition. The order of the operators
in the original expression is reversed in the resulting postfix
expression.

As we process the expression, the operators have to be saved somewhere
since their corresponding right operands are not seen yet. Also, the
order of these saved operators may need to be reversed due to their
precedence. This is the case with the addition and the multiplication in
this example. Since the addition operator comes before the
multiplication operator and has lower precedence, it needs to appear
after the multiplication operator is used. Because of this reversal of
order, it makes sense to consider using a stack to keep the operators
until they are needed.

What about (A + B) · C? Recall that A B + C · is the postfix
equivalent. Again, processing this infix expression from left to right,
we see + first. In this case, when we see ·, + has already been placed
in the result expression because it has precedence over · by virtue of
the parentheses. We can now start to see how the conversion algorithm
will work. When we see a left parenthesis, we will save it to denote
that another operator of high precedence will be coming. That operator
will need to wait until the corresponding right parenthesis appears to
denote its position (recall the fully parenthesized technique). When
that right parenthesis does appear, the operator can be popped from the
stack.

As we scan the infix expression from left to right, we will use a stack
to keep the operators. This will provide the reversal that we noted in
the first example. The top of the stack will always be the most recently
saved operator. Whenever we read a new operator, we will need to
consider how that operator compares in precedence with the operators, if
any, already on the stack.

Assume the infix expression is a string of tokens delimited by spaces.
The operator tokens are ·, /, +, and -, along with the left and right
parentheses, ( and ). The operand tokens are the single-character
identifiers A, B, C, and so on. The following steps will produce a
string of tokens in postfix order.

#. Create an empty stack called ``op_stack`` for keeping operators.
   Create an empty list for output.

#. Convert the input infix string to a list by using the string method
   ``split``.

#. Scan the token list from left to right.

   -  If the token is an operand, append it to the end of the output
      list.

   -  If the token is a left parenthesis, push it on the ``op_stack``.

   -  If the token is a right parenthesis, pop the ``op_stack`` until the
      corresponding left parenthesis is removed. Append each operator to
      the end of the output list.

   -  If the token is an operator, ·, /, +, or -, push it on the
      ``op_stack``. However, first remove any operators already on the
      ``op_stack`` that have higher or equal precedence and append them
      to the output list.

#. When the input expression has been completely processed, check the
   ``op_stack``. Any operators still on the stack can be removed and
   appended to the end of the output list.

:ref:`Figure 9 <fig_intopost>` shows the conversion algorithm working on the
expression A · B + C · D. Note that the first · operator is removed
upon seeing the + operator. Also, + stays on the stack when the second
· occurs, since multiplication has precedence over addition. At the end
of the infix expression the stack is popped twice, removing both
operators and placing + as the last operator in the postfix expression.

.. _fig_intopost:

.. figure:: Figures/intopost.png
   :align: center

   Figure 9: Converting A · B + C · D to Postfix Notation

In order to code the algorithm in Python, we will use a dictionary
called ``prec`` to hold the precedence values for the operators,
as seen in in :ref:`ActiveCode 1 <lst_intopost>`. This
dictionary will map each operator to an integer that can be compared
against the precedence levels of other operators (we have arbitrarily
used the integers 3, 2, and 1). The left parenthesis will receive the
lowest value possible. This way any operator that is compared against it
will have higher precedence and will be placed on top of it.
Line 15 defines the operands to be any upper-case character or digit.

.. _lst_intopost:


.. activecode:: intopost
    :caption: Converting Infix Expressions to Postfix Expressions
    :nocodelens:

    from pythonds3.basic import Stack

    def infix_to_postfix(infix_expr):
        prec = {}
        prec["*"] = 3
        prec["/"] = 3
        prec["+"] = 2
        prec["-"] = 2
        prec["("] = 1
        op_stack = Stack()
        postfix_list = []
        token_list = infix_expr.split()

        for token in token_list:
            if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
                postfix_list.append(token)
            elif token == "(":
                op_stack.push(token)
            elif token == ")":
                top_token = op_stack.pop()
                while top_token != "(":
                    postfix_list.append(top_token)
                    top_token = op_stack.pop()
            else:
                while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                    postfix_list.append(op_stack.pop())
                op_stack.push(token)

        while not op_stack.is_empty():
            postfix_list.append(op_stack.pop())

        return " ".join(postfix_list)

    print(infix_to_postfix("A * B + C * D"))
    print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))

--------------

A few more examples of execution in the Python shell are shown below.

::

    >>> infix_to_postfix("( A + B ) * ( C + D )")
    'A B + C D + *'
    >>> infix_to_postfix("( A + B ) * C")
    'A B + C *'
    >>> infix_to_postfix("A + B * C")
    'A B C * +'
    >>>

Postfix Evaluation
^^^^^^^^^^^^^^^^^^

As a final stack example, we will consider the evaluation of an
expression that is already in postfix notation. In this case, a stack is
again the data structure of choice. However, as you scan the postfix
expression, it is the operands that must wait, not the operators as in
the conversion algorithm above. Another way to think about the solution
is that whenever an operator is seen on the input, the two most recent
operands will be used in the evaluation.

To see this in more detail, consider the postfix expression
4 5 6 · +. As you scan the expression from left to right, you first
encounter the operands 4 and 5. At this point, you are still unsure what
to do with them until you see the next symbol. Placing each on the stack
ensures that they are available if an operator comes next.

In this case, the next symbol is another operand. So, as before, push it
and check the next symbol. Now we see an operator, ·. This means that
the two most recent operands need to be used in a multiplication
operation. By popping the stack twice, we can get the proper operands
and then perform the multiplication (in this case getting the result
30).

We can now handle this result by placing it back on the stack so that it
can be used as an operand for the later operators in the expression.
When the final operator is processed, there will be only one value left
on the stack. Pop and return it as the result of the expression.
:ref:`Figure 10 <fig_evalpost1>` shows the stack contents as this entire example
expression is being processed.

.. _fig_evalpost1:

.. figure:: Figures/evalpostfix1.png
   :align: center

   Figure 10: Stack Contents During Evaluation


:ref:`Figure 11 <fig_evalpost2>` shows a slightly more complex example, 7 8 + 3 2
+ /. There are two things to note in this example. First, the stack size
grows, shrinks, and then grows again as the subexpressions are
evaluated. Second, the division operation needs to be handled carefully.
Recall that the operands in the postfix expression are in their original
order since postfix changes only the placement of operators. When the
operands for the division are popped from the stack, they are reversed.
Since division is *not* a commutative operator, in other words
:math:`15/5` is not the same as :math:`5/15`, we must be sure that
the order of the operands is not switched.

.. _fig_evalpost2:

.. figure:: Figures/evalpostfix2.png
   :align: center

   Figure 11: A More Complex Example of Evaluation


Assume the postfix expression is a string of tokens delimited by spaces.
The operators are ·, /, +, and - and the operands are assumed to be
single-digit integer values. The output will be an integer result.

#. Create an empty stack called ``operand_stack``.

#. Convert the string to a list by using the string method ``split``.

#. Scan the token list from left to right.

   -  If the token is an operand, convert it from a string to an integer
      and push the value onto the ``operand_stack``.

   -  If the token is an operator, ·, /, +, or -, it will need two
      operands. Pop the ``operand_stack`` twice. The first pop is the
      second operand and the second pop is the first operand. Perform
      the arithmetic operation. Push the result back on the
      ``operand_stack``.

#. When the input expression has been completely processed, the result
   is on the stack. Pop the ``operand_stack`` and return the value.

The complete function for the evaluation of postfix expressions is shown
in :ref:`ActiveCode 2 <lst_postfixeval>`. To assist with the arithmetic, a helper
function ``do_math`` is defined. It will take two operands and an
operator and then perform the proper arithmetic operation.

.. _lst_postfixeval:

.. activecode:: postfixeval
    :caption: Postfix Evaluation
    :nocodelens:

    from pythonds3.basic import Stack

    def postfix_eval(postfix_expr):
        operand_stack = Stack()
        token_list = postfix_expr.split()

        for token in token_list:
            if token in "0123456789":
                operand_stack.push(int(token))
            else:
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                result = do_math(token, operand1, operand2)
                operand_stack.push(result)
        return operand_stack.pop()


    def do_math(op, op1, op2):
        if op == "*":
            return op1 * op2
        elif op == "/":
            return op1 / op2
        elif op == "+":
            return op1 + op2
        else:
            return op1 - op2


    print(postfix_eval("7 8 + 3 2 + /"))

It is important to note that in both the postfix conversion and the
postfix evaluation programs we assumed that there were no errors in the
input expression. Using these programs as a starting point, you can
easily see how error detection and reporting can be included. We leave
this as an exercise at the end of the chapter.

.. admonition:: Self Check

   .. fillintheblank:: postfix1

      Without using the activecode ``infix_to_postfix`` function, convert the following expression to postfix  ``10 + 3 * 5 / (16 - 4)`` .

      |blank|

      -  :10\s+3\s+5\s*\*\s*16\s+4\s*-\s*/\s*\+: Correct.
         :10.*3.*5.*16.*4\s+[ /+*-]*: The numbers appear to be in the correct order check your operators
         :x: Remember the numbers will be in the same order as the original equation


   .. fillintheblank:: postfix2

      What is the result of evaluating the following: ``17 10 + 3 * 9 / ==`` ?

      |blank|

      -  :9: Correct.
         :x: Remember to push each intermediate result back on the stack


   .. fillintheblank:: postfix3

      Modify the ``infix_to_postfix`` function so that it can convert the following expression:  ``5 * 3 ^ (4 - 2)``. Run the function on the expression and paste the answer here:

      |blank|

      -  :5\s+3\s+4\s+2\s*-\s*\*\*\s*\*: Correct.
         :x: Hint: You only need to add one line to the function!!

.. youtube:: LO-2q4pSsdM
    :divid: video_Stack3
    :height: 315
    :width: 560
    :align: left
