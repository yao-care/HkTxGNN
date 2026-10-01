---
layout: default
title: Ibuprofen
parent: 僅模型預測 (L5)
nav_order: 444
evidence_level: L5
indication_count: 5
---

# Ibuprofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Ibuprofen：從解熱鎮痛消炎到肢中骨發育不良（Hunter-Thompson 型）

## 一句話總結

Ibuprofen（布洛芬）是常見的非類固醇消炎止痛藥（NSAID），在香港已有多張許可證。
TxGNN 模型預測它可能對**肢中骨發育不良，Hunter-Thompson 型 (Acromesomelic dysplasia, Hunter-Thompson type)** 有效，預測分數很高。
但目前**沒有任何臨床試驗或文獻**支持，屬於純模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 肢中骨發育不良，Hunter-Thompson 型 (Acromesomelic dysplasia, Hunter-Thompson type) |
| TxGNN 預測分數 | 99.74% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Ibuprofen 一般已知是非選擇性 COX-1/COX-2 抑制劑，透過抑制前列腺素合成來達到消炎與止痛效果。

Hunter-Thompson 型肢中骨發育不良是罕見的遺傳性骨骼發育異常，主要影響肢體生長與形態。前列腺素抑制與這類疾病的致病機轉之間，**沒有已知的關聯**。頂多只能推測 NSAID 對伴隨的疼痛有症狀緩解作用，這並不是改變疾病本身的治療。

這個高分預測較可能來自知識圖譜中的鄰近節點特徵（例如相近的骨骼或疼痛相關疾病），而不是已被證實的生物學依據。

其他排名前 5 的預測也有相同問題，都是罕見遺傳或先天畸形疾病，都沒有機轉或臨床證據：

| 排名 | 預測疾病 | TxGNN 分數 |
|------|---------|-----------|
| 2 | 短軀幹發育不良合併釉質發育不全症候群 (Brachyolmia-amelogenesis imperfecta syndrome) | 99.71% |
| 3 | 肌硬化症 (Myosclerosis) | 99.68% |
| 4 | 短軀幹發育不良 (Brachyolmia) | 99.67% |
| 5 | 短指併指症候群 (Brachydactyly-syndactyly syndrome) | 99.66% |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 20 張含 Ibuprofen 的許可證，以下列出 5 張：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-55058 | INFACALM IBUPROFEN INFANT DROPS 40MG/ML | TIANDA PHARMACEUTICALS LIMITED |
| HK-43233 | BUPOGESIC 200 TAB 200MG | VICKMANS LABORATORIES LTD |
| HK-67025 | WILLIPO IBUPROFEN TABLETS 200MG | WELLDONE PHARMACEUTICALS LIMITED |
| HK-51501 | NUROFEN GEL 5%W/W | RECKITT BENCKISER HONG KONG LTD |
| HK-51805 | AMBUFEN 400 TAB 400MG | NATURAL HEALTH RESOURCES COMPANY LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這項預測只有模型分數，沒有臨床試驗、文獻或明確的機轉支持（L5）。
- Ibuprofen 的 COX 抑制作用無法合理解釋對骨骼發育異常的療效。

**若要推進需要：**
- 補齊 Ibuprofen 的作用機轉與原適應症資料（可查詢 DrugBank）。
- 取得香港衛生署核准的仿單，完成警語與禁忌症的安全性篩選。
- 有文獻或動物模型顯示 COX／前列腺素路徑與此疾病有關，才值得重新評估。
- 若只是要緩解此類疾病的疼痛，應改以症狀治療為目標重新定義適應症，不宜視為疾病修飾治療。

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

