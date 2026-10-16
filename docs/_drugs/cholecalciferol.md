---
layout: default
title: Cholecalciferol
parent: 僅模型預測 (L5)
nav_order: 192
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Cholecalciferol：預測新適應症為腎性骨病變 (Renal Osteodystrophy)（證據等級 L5）。原適應症：骨質疏鬆、停經後骨質疏鬆、佝僂病、骨軟化症、維生素 D 缺乏、副甲狀腺低下等"
---

# Cholecalciferol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Cholecalciferol：從骨質疏鬆與維生素 D 缺乏到腎性骨病變

## 一句話總結

Cholecalciferol（維生素 D3）原本用於骨質疏鬆、佝僂病、骨軟化症、維生素 D 缺乏及副甲狀腺低下等疾病。
TxGNN 模型預測它可能對**腎性骨病變 (Renal Osteodystrophy)** 有效（本報告所有預測中證據最完整者），
目前有 **2 個臨床試驗**和 **20 篇文獻**與此方向相關，但直接證據有限。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 骨質疏鬆、停經後骨質疏鬆、佝僂病、骨軟化症、維生素 D 缺乏、副甲狀腺低下等（香港許可證未登載適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 腎性骨病變 (Renal Osteodystrophy) |
| TxGNN 預測分數 | 99.11% |
| 證據等級 | L1（依資料編譯時的評分；但實際僅 1 項 Phase 3 RCT 且狀態不明，保守來看應視為 L2 以下） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 13 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，cholecalciferol 是維生素 D 的天然形式（前驅荷爾蒙），
需在肝臟轉為 25(OH)D，再於腎臟轉為活性的 1,25-二羥基維生素 D。
其在骨質疏鬆、佝僂病、骨軟化症等骨礦物質代謝疾病中的角色已確立，機轉上可能適用於腎性骨病變。

在慢性腎臟病的礦物質與骨骼異常（CKD-MBD）中，維生素 D 缺乏會促成次發性副甲狀腺亢進與骨病變。
補充 cholecalciferol 可補足 25(OH)D 受質，供腎外組織局部活化並協助抑制 PTH。
這與其原本在骨代謝疾病的用途高度相關。

需注意的限制：在晚期 CKD，腎臟 1-α 羟化能力下降，單用天然維生素 D 可能不足以充分抑制 PTH，
骨骼終點的療效仍不明確。

其他排名較前的預測（如家族性孤立性副甲狀腺低下、肢中發育不良等罕見遺傳病）皆無臨床試驗，
缺乏合理的機轉連結，建議維持 Hold。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00752401](https://clinicaltrials.gov/study/NCT00752401) | Phase 3 | 未知 | 200 | 在維生素 D 缺乏的腎臟移植受者中，隨機、安慰劑對照評估補充 cholecalciferol 對移植後結果（腎絲球過濾率、肌酸酐、急性排斥、感染）的影響；未提供結果，且族群為移植者，對腎性骨病變僅間接相關 |
| [NCT00285467](https://clinicaltrials.gov/study/NCT00285467) | NA | 完成 | 55 | 比較 cholecalciferol 與 doxercalciferol 治療 CKD 次發性副甲狀腺亢進；與腎性骨病變核心機轉直接相關，但樣本小、非 Phase 3 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [34747516](https://pubmed.ncbi.nlm.nih.gov/34747516/) | 2022 | RCT 次要終點分析 | J Bone Miner Res | 補充 cholecalciferol 可減緩腎移植受者的骨質流失 |
| [35200136](https://pubmed.ncbi.nlm.nih.gov/35200136/) | 2022 | 前瞻性對照研究 | Clin Nephrol | 評估維生素 D 類固醇對透析前 CKD 患者骨組織學的影響 |
| [38397979](https://pubmed.ncbi.nlm.nih.gov/38397979/) | 2024 | 臨床（觀察）研究 | Biomedicines | 高劑量 cholecalciferol 用於血液透析患者的療效與安全性 |
| [30274806](https://pubmed.ncbi.nlm.nih.gov/30274806/) | 2019 | Review | Nefrologia | 透析前 CKD 使用天然維生素 D 的角色仍不明確 |
| [33922902](https://pubmed.ncbi.nlm.nih.gov/33922902/) | 2021 | Review | Nutrients | 維生素 D 對 CKD 與腎移植患者骨穩態及心血管的影響 |
| [20671739](https://pubmed.ncbi.nlm.nih.gov/20671739/) | 2010 | Review | Kidney Int Suppl | 腎性骨病變、次發性副甲狀腺亢進與維生素 D 缺乏和 CKD 死亡率相關 |
| [30297082](https://pubmed.ncbi.nlm.nih.gov/30297082/) | 2018 | 工作坊報告 | Am J Kidney Dis | CKD 3–4 期維生素 D 評估與處置仍有爭議 |
| [23713880](https://pubmed.ncbi.nlm.nih.gov/23713880/) | 2014 | Review | Curr Vasc Pharmacol | 天然維生素 D 與 calcifediol 在 CKD-MBD 的治療角色 |
| [21947120](https://pubmed.ncbi.nlm.nih.gov/21947120/) | 2011 | Review | Nat Rev Nephrol | 兒童 CKD 的礦物質與骨骼異常 |
| [39597015](https://pubmed.ncbi.nlm.nih.gov/39597015/) | 2024 | 觀察性前瞻研究 | Medicina | 血液透析患者以 cholecalciferol 達到較高 25(OH)D 的可能益處 |

---

## 香港上市資訊

香港共有 13 張有效單一成分許可證，以下列出 5 張主要許可證（資料中未登載劑型與核准適應症文字）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67080 | VITA GREEN VITAMIN D3 TABLETS 1200IU | 未登載 | 未登載 |
| HK-68740 | DECUROL CAPSULES 25000IU | 未登載 | 未登載 |
| HK-68743 | DECUROL ORAL DROPS 2400IU/ML | 未登載 | 未登載 |
| HK-56397 | FOSAMAX PLUS TAB 70MG/5600IU（含 alendronate） | 未登載 | 未登載 |
| HK-65828 | APO-ALENDRONATE/VITAMIN D3 TABLETS 70MG/70MCG | 未登載 | 未登載 |

---

## 安全性考量

- **主要警語與禁忌症**：香港仿單的警語與禁忌症資料尚未取得，請參考原廠仿單。
- **知識圖譜標示的禁忌相關疾病**（非仿單文字）：包括高血壓、腎臟疾病、肝病、結節病、高副甲狀腺素血症、高鈣血症、腎鈣化症、磷代謝異常、原發性高草酸尿症、血色素沉著症、威爾森氏症、乳癌、攝護腺癌、高脂血症等。
  特別是**腎臟疾病、高鈣血症、腎鈣化症**與本預測的目標族群（CKD）直接相關，需審慎評估。
- **藥物交互作用**：共 56 筆，列出的前 20 筆中，**重大 (Major)** 交互作用為活性維生素 D 類與類似物：calcifediol、calcitriol、dihydrotachysterol、doxercalciferol（併用有高鈣血症風險）。
  **中度 (Moderate)** 包括 thiazide 類利尿劑（bendroflumethiazide、chlorothiazide、chlorthalidone 等）、巴比妥類（amobarbital、butabarbital、butalbital）、carbamazepine、膽酸結合劑（cholestyramine、colesevelam、colestipol）、digoxin 與 digitoxin。
  cimetidine 為輕微 (Minor)。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 腎性骨病變是所有預測中唯一同時有臨床試驗（含 1 項 Phase 3 RCT）與較多文獻支持的方向，且與 cholecalciferol 的原有用途機轉相近。
- 但 Phase 3 試驗針對的是腎移植族群且狀態未知、無結果，另一項試驗樣本小、非 Phase 3，直接證據不足，因此需設定防護條件。
- 其餘預測（家族性孤立性副甲狀腺低下、肢中發育不良、顱面錐形發育不良、Dahlberg-Borer-Newcomer 症候群、腎小管酸中毒）無有效證據，建議 Hold；低磷性佝僂病僅屬研究問題階段，天然維生素 D 並非主要治療。

**若要推進需要：**
- 取得 NCT00752401 的結果，並確認其與腎性骨病變終點的相關性
- 設計針對 CKD-MBD 的隨機試驗，以骨組織學、骨密度、PTH 為終點，並依 CKD 分期設定劑量
- 監測鈣、磷、PTH 與 25(OH)D，避免高鈣血症與血管鈣化
- 評估與活性維生素 D 類、thiazide 類利尿劑併用的風險
- 取得香港仿單的警語、禁忌症與作用機轉資料
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

