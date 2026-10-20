---
layout: default
title: Ergocalciferol
parent: 僅模型預測 (L5)
nav_order: 333
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ergocalciferol：預測新適應症為腎性骨失養症 (Renal Osteodystrophy)（證據等級 L5）。原適應症：骨質疏鬆、停經後骨質疏鬆、維生素 D 缺乏、骨軟化症、佝僂病、副甲狀腺低下等"
monitor_inn: "ERGOCALCIFEROL"
predicted_indications: ["familial isolated hypoparathyroidism due to impaired PTH secretion", "acromesomelic dysplasia, Campailla Martinelli type", "renal tubular acidosis", "craniofacial conodysplasia", "Dahlberg-Borer-Newcomer syndrome", "hypophosphatemia (disease)", "renal osteodystrophy", "calcium-alkali syndrome", "vitamin D-dependent rickets"]
---

# Ergocalciferol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

# Ergocalciferol：從骨質疏鬆與維生素 D 缺乏相關疾病到腎性骨失養症

## 一句話總結

Ergocalciferol（維生素 D2）原本用於骨質疏鬆、佝僂病、骨軟化症、副甲狀腺低下等鈣磷代謝相關疾病。
TxGNN 模型的首位預測為**家族性孤立性副甲狀腺低下症**，但該預測僅有模型分數，沒有任何實際研究支持。
本報告另外挑出證據最完整的預測：**腎性骨失養症 (Renal Osteodystrophy)**，目前有 **1 個臨床試驗**和 **20 篇文獻**支持。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 骨質疏鬆、停經後骨質疏鬆、維生素 D 缺乏、骨軟化症、佝僂病、副甲狀腺低下等（香港許可證未載明適應症文字，此為知識圖譜所列適應症） |
| 預測新適應症 | 腎性骨失養症 (Renal Osteodystrophy)（證據最完整者；TxGNN 排名第 1 的預測為家族性孤立性副甲狀腺低下症，分數 99.85%，僅 L5） |
| TxGNN 預測分數 | 99.67%（腎性骨失養症） |
| 證據等級 | L2（但試驗狀態不明、設計與結果未能確認，保守看待） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，ergocalciferol 是維生素 D2，屬於天然（營養性）維生素 D，在體內需經肝臟與腎臟羥化後才成為活性型 1,25-二羥維生素 D。

慢性腎臟病 (CKD) 患者常有 25-羥維生素 D 不足，進而促成次發性副甲狀腺機能亢進與礦物質骨代謝異常，這正是腎性骨失養症的基礎。補充 ergocalciferol 可提供 25-羥維生素 D 的受質，供腎外組織及殘餘腎功能進行 1-α 羥化。這與其原有的維生素 D 缺乏、骨軟化症、佝僂病等適應症在骨礦化機轉上相連。

不過，現有證據對硬性臨床結果（如死亡率、骨折）的結論並不一致，且腎功能嚴重受損者轉換活性型的能力有限，因此需與活性維生素 D（如 calcitriol、doxercalciferol）的角色一併評估。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01799317](https://clinicaltrials.gov/study/NCT01799317) | Phase 4 | 未知 | 60 | 評估 ergocalciferol 合併 doxercalciferol，或單用 doxercalciferol，能否矯正接受腹膜透析、併有次發性副甲狀腺機能亢進之兒童的骨礦化缺陷（2009-03 至 2014-06）；未提供結果 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27401037](https://pubmed.ncbi.nlm.nih.gov/27401037/) | 2016 | 隨機對照試驗（比較研究） | Eur J Pharmacol | 204 名 CKD 3-5 期病人，比較 ergocalciferol 與 calcitriol 控制礦物質骨代謝異常的療效與安全性，追蹤約 33 個月 |
| [3877585](https://pubmed.ncbi.nlm.nih.gov/3877585/) | 1985 | 臨床研究（兒童） | Clin Nephrol | 18 名慢性腎衰竭兒童，比較 calcitriol 與 ergocalciferol 對骨組織學與生長的影響 |
| [30274806](https://pubmed.ncbi.nlm.nih.gov/30274806/) | 2019 | Review | Nefrologia | 透析前 CKD 使用天然維生素 D 的角色仍不明確 |
| [28873969](https://pubmed.ncbi.nlm.nih.gov/28873969/) | 2017 | 臨床實務建議 | Nephrol Dial Transplant | CKD 2-5 期及透析兒童的天然維生素 D 治療建議 |
| [30297082](https://pubmed.ncbi.nlm.nih.gov/30297082/) | 2018 | 專家工作坊報告 | Am J Kidney Dis | 討論 CKD 3-4 期維生素 D 的爭議與管理 |
| [20671739](https://pubmed.ncbi.nlm.nih.gov/20671739/) | 2010 | Review | Kidney Int Suppl | 腎性骨病、礦物質異常與 CKD 死亡率的關聯 |
| [21947120](https://pubmed.ncbi.nlm.nih.gov/21947120/) | 2011 | Review | Nat Rev Nephrol | 兒童 CKD 的礦物質與骨代謝異常 |
| [16898852](https://pubmed.ncbi.nlm.nih.gov/16898852/) | 2006 | Review | Paediatr Drugs | 減少腎衰竭兒童骨骼異常的策略 |
| [23713880](https://pubmed.ncbi.nlm.nih.gov/23713880/) | 2014 | Review | Curr Vasc Pharmacol | 原型維生素 D 與 calcifediol 在 CKD-MBD 的角色 |
| [34626363](https://pubmed.ncbi.nlm.nih.gov/34626363/) | 2022 | Review | J Nephrol | 緩釋 calcifediol 用於 CKD 3-4 期次發性副甲狀腺機能亢進 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-36205 | VITALIPID N INFANT INJ | 未載明 | 未載明 |
| HK-36206 | VITALIPID N ADULT INJ | 未載明 | 未載明 |
| HK-01178 | POLIBABY CREAM | 未載明 | 未載明 |
| HK-52479 | AMINOLEBAN EN POWDER | 未載明 | 未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自藥物與疾病關聯資料，並非仿單原文）：高血壓、腎臟病、肝病、膽囊疾病、類肉瘤病、糖尿病、心房顫動、副甲狀腺機能亢進、高鈣血症、腎鈣化症、磷代謝異常、血液凝固疾病、鐮刀型貧血、原發性高草酸尿症、血色素沉著症、威爾森氏症、高脂血症、乳癌、攝護腺癌等。其中腎臟病與本預測適應症的族群高度重疊，須特別謹慎。
- **藥物交互作用**：共查得 55 筆，主要包括：
  - 重大 (Major)：cholecalciferol、calcifediol、calcitriol、doxercalciferol（與其他維生素 D 類藥物併用有高鈣風險）
  - 中度 (Moderate)：噻嗪類利尿劑（hydrochlorothiazide、chlorothiazide、chlorthalidone）、含鎂制酸劑（magnesium oxide）、膽酸結合劑（cholestyramine、colestipol、colesevelam）、sevelamer、carbamazepine、barbiturates、rifabutin、digoxin 等

仿單的主要警語與禁忌資料目前缺漏，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 腎性骨失養症是所有預測中證據最完整者，有 1 個 Phase 4 試驗及數項 ergocalciferol 與 calcitriol 的比較研究，機轉也合理。
- 但該試驗狀態不明、無結果，文獻多為綜述，對硬性臨床結果的結論不一致，故宜在監測防護下推進，而非直接採用。

**其他預測的處置：**
- 家族性孤立性副甲狀腺低下症、顱面錐形發育不良、肢中段發育不良（Campailla-Martinelli 型）、鈣鹼症候群：無試驗與文獻，建議 Hold。其中鈣鹼症候群涉及高鈣血症，更可能是風險而非治療機會。
- 腎小管酸中毒、Dahlberg-Borer-Newcomer 症候群：文獻為個案報告或不相關的一般維生素 D 文獻，無法支持。
- 低磷血症、低磷性佝僂病、維生素 D 依賴型佝僂病：屬研究問題，證據多為舊的個案或生理研究。其中低磷性佝僂病本為原有適應症；第 I 型維生素 D 依賴型佝僂病因無法轉換為活性型，機轉上受限。

**若要推進需要：**
- 確認 NCT01799317 的結果，並確認 ergocalciferol 與 calcitriol 比較研究的實際設計與主要結果
- 取得詳細的作用機轉資料，以及香港仿單的警語與禁忌
- 訂定監測計畫：血鈣、血磷、PTH、25-羥維生素 D，避免高鈣血症與骨轉換過度抑制
- 評估與活性維生素 D、磷結合劑（如 sevelamer）併用的交互作用風險
- 釐清香港許可證品項皆為複方或營養製劑，目前無單方 ergocalciferol 製劑，需評估劑型與給藥途徑的可行性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

