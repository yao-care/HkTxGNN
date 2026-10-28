---
layout: default
title: Potassium Citrate
parent: 僅模型預測 (L5)
nav_order: 719
evidence_level: L5
indication_count: 9
monitor_inn: "POTASSIUM CITRATE"
predicted_indications: ["familial visceral myopathy", "mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "Pendred syndrome", "nephrolithiasis", "cystinosis", "autosomal recessive nonsyndromic deafness", "exocrine pancreatic insufficiency", "leukocyte adhesion deficiency", "adult Fanconi syndrome"]
last_modified_at: 2026-10-23
description: "Potassium Citrate：預測新適應症為家族性內臟肌病變 (familial visceral myopathy)（證據等級 L5）."
---

# Potassium Citrate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Potassium Citrate：從鉀缺乏症與腎小管酸中毒到家族性內臟肌病
{: .text-alpha }

## 一句話總結

Potassium Citrate（檸檬酸鉀）在知識圖譜中記錄的用途包括鉀缺乏症、腎小管酸中毒與急性尿酸腎病變。
TxGNN 模型預測排名第一的是**家族性內臟肌病變 (familial visceral myopathy)**，但這項預測沒有任何證據支持；證據最充分的預測是**腎結石 (Nephrolithiasis)**，目前有 **15 個臨床試驗**和 **16 篇文獻**，但這些研究多為替代指標或機轉層面的研究。

> 本報告以預測排名第 1 的疾病作為標題與快速總覽，並另列證據最完整的腎結石作為重點評估。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 知識圖譜記錄的相關適應症 | 鉀缺乏症、腎小管酸中毒、急性尿酸腎病變（此為知識圖譜關聯，非香港核准適應症） |
| 預測新適應症（排名第 1） | 家族性內臟肌病變 (familial visceral myopathy) |
| TxGNN 預測分數（排名第 1） | 0.9995 |
| 證據等級（排名第 1） | L5 |
| 證據最完整的預測 | 家族性內臟肌病 |
| 證據等級（腎結石） | L5（見下方說明） |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策（排名第 1） | Hold |
| 建議決策（腎結石） | Proceed with Guardrails |

> **證據等級說明：** 腎結石的試驗有直接研究疾病本身（例如 NCT00004284 為 Phase 3 隨機雙盲試驗，但該試驗比較磷酸鉀與檸檬酸鉀，狀態為完成，卻缺乏已發表結果；NCT06819553 為 Phase 2/3，狀態未知）。依本報告的分級標準，L1–L3 需有已完成且有結果的 RCT 或系統性回顧支持。目前資料中，可直接對應腎結石的研究包括一篇系統性回顧與統合分析（PMID 27915395），其研究主題為檸檬酸鉀補充對碎石前後結石復發的影響，屬直接研究腎結石，故評為 **L3**。系統內部評分為 L2，本報告採較保守的 L3。

> 修正：快速總覽中腎結石證據等級應為 **L3**（而非 L5），特此更正。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA）。根據已知資訊，檸檬酸鉀提供鉀離子與檸檬酸鹽鹼性負荷，檸檬酸鹽在體內代謝為碳酸氫鹽。

**腎結石（證據最完整）：** 檸檬酸鹽代謝後使尿液 pH 上升、尿檸檬酸排泄增加。檸檬酸可與鈣結合，抑制草酸鈣與磷酸鈣結晶的成核與生長，鹼化尿液也有助於溶解尿酸結石。此機轉與知識圖譜中記錄的腎小管酸中毒、低檸檬酸尿相關用途一致。需注意：對磷酸鈣結石，過度鹼化可能提高過飽和度，需謹慎。此用途大致屬於既有用途，而非全新的藥物再利用。

**排名第 1 的家族性內臟肌病（0.9995）：** 這是腸道平滑肌的遺傳疾病（如 ACTG2 變異），檸檬酸鉀對其病理無已知作用。高分來自 TxGNN 模型（深度學習），可能反映模型在相關疾病間學到的相似性，不是生物學證據，沒有臨床或文獻佐證，機轉上找不到合理連結。

**其他預測：** 胱胺酸症與成人范可尼症候群涉及近端腎小管的碳酸氫鹽與鉀流失，檸檬酸鉀可作為支持性治療，但不改變疾病本質。外分泌胰臟功能不全可能透過腸道高草酸尿症間接增加結石風險，檸檬酸鉀只針對併發症。其餘（粒線體 OXPHOS 疾病、Pendred 症候群、遺傳性聾、白血球黏附缺乏症）沒有合理機轉。

---

## 臨床試驗證據

以下為腎結石（證據最完整的預測）相關試驗，排名第 1 的疾病無臨床試驗登記。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00004284](https://clinicaltrials.gov/study/NCT00004284) | Phase 3 | 完成 | 300 | 比較緩釋磷酸鉀與檸檬酸鉀對吸收性高鈣尿症的結石預防 |
| [NCT02373384](https://clinicaltrials.gov/study/NCT02373384) | Phase 4 | 完成 | 182 | 口服溶解療法於可透 X 光腎結石的成功預測因子 |
| [NCT06819553](https://clinicaltrials.gov/study/NCT06819553) | Phase 2/3 | 未知 | 48 | 口服檸檬酸鉀減少輸尿管支架結痂（尿酸結石輸尿管鏡術後） |
| [NCT01754779](https://clinicaltrials.gov/study/NCT01754779) | Phase 2 | 完成 | 13 | 檸檬酸或檸檬酸鉀能否降低磷酸鈣結石患者尿液飽和度 |
| [NCT06966635](https://clinicaltrials.gov/study/NCT06966635) | Phase 4 | 招募中 | 312 | 檸檬酸鉀緩釋錠用於痛風，探討降尿酸與預防尿路結石 |
| [NCT03984409](https://clinicaltrials.gov/study/NCT03984409) | N/A | 完成 | 22 | 低熱量柳橙汁作為檸檬酸鉀的飲食來源，改善低檸檬酸尿 |
| [NCT03836144](https://clinicaltrials.gov/study/NCT03836144) | N/A | 完成 | 63 | 胱胺酸尿症患者尿液鹼化對尿液發炎標記的影響 |
| [NCT05389995](https://clinicaltrials.gov/study/NCT05389995) | N/A | 進行中（不再招募） | 10 | 檸檬水飲品與檸檬酸鉀對尿路結石風險因子的影響 |
| [NCT03281928](https://clinicaltrials.gov/study/NCT03281928) | N/A | 已終止 | 30 | 飲食中鈉與檸檬酸鉀對腎臟礦物質處理的影響 |
| [NCT01980004](https://clinicaltrials.gov/study/NCT01980004) | Phase 2 | 已撤回 | 0 | 磷酸鈣結石復發預防（未收案，無證據產出） |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27915395](https://pubmed.ncbi.nlm.nih.gov/27915395/) | 2017 | 系統性回顧與統合分析 | Urolithiasis | 檸檬酸鉀補充對碎石前後結石復發的影響 |
| [40978115](https://pubmed.ncbi.nlm.nih.gov/40978115/) | 2025 | Review | Clin Kidney J | 檸檬酸在腎生理中的角色及其對鈣結石的抑制 |
| [30531474](https://pubmed.ncbi.nlm.nih.gov/30531474/) | 2019 | Review | Curr Opin Nephrol Hypertens | 檸檬酸治療磷酸鈣結石的角色，效果不一致 |
| [30478476](https://pubmed.ncbi.nlm.nih.gov/30478476/) | 2019 | Review | Urolithiasis | 腎結石的經驗性治療 |
| [26977089](https://pubmed.ncbi.nlm.nih.gov/26977089/) | 2016 | Review | BMJ | 腎結石的內科處置 |
| [40583613](https://pubmed.ncbi.nlm.nih.gov/40583613/) | 2025 | Review | Arch Ital Urol Androl | 泌尿道結石專家管理共識 |
| [11475849](https://pubmed.ncbi.nlm.nih.gov/11475849/) | 2001 | 治療綜述 | Przegl Lek | 檸檬酸鉀的治療適應症，含草酸鈣結石、部分尿酸結石與遠端腎小管酸中毒 |
| [18518781](https://pubmed.ncbi.nlm.nih.gov/18518781/) | 2008 | 綜述 | Expert Opin Pharmacother | 腎結石藥物治療 |
| [23924538](https://pubmed.ncbi.nlm.nih.gov/23924538/) | 2013 | Review | Medicina | 檸檬酸與腎結石，低檸檬酸尿的成因 |
| [8352061](https://pubmed.ncbi.nlm.nih.gov/8352061/) | 1993 | 觀察性研究 | J Bone Miner Res | 鹼吸收與檸檬酸排泄於鈣結石的關係 |

其餘預測（胱胺酸症、外分泌胰臟功能不全、成人范可尼症候群）僅有個案報告，且均未評估檸檬酸鉀作為介入；排名第 1 的疾病無任何文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-47513 | UROCIT-K TAB 1080MG | 未提供 | 未提供 |

此許可證為單方製劑，狀態有效。因許可證未提供適應症文字，本報告無法以香港許可證確認核准適應症；上述原適應症僅為知識圖譜記錄。

---

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單內容）：高血壓、腎臟疾病、腎功能不全、無尿、腎上腺功能不全／Addison 病、消化性潰瘍、高鈣血症、腎鈣質沉著症、心肌梗塞、冠狀動脈疾病、橫紋肌溶解、代謝性酸中毒、腹瀉性疾病、胰臟炎、良性攝護腺增生等。
- **藥物交互作用**（共查得 100 筆，以下為部分）：
  - 主要 (Major)：Amiloride、Benazepril、Olmesartan、Valsartan（高血鉀風險）；Chlorpheniramine、Acrivastine、Atropine、Hyoscyamine、Methscopolamine、Homatropine、Phenyltoloxamine、Amitriptyline（抗膽鹼相關）
  - 中度 (Moderate)：Aliskiren、Ibuprofen、Ketorolac、Acetylsalicylic acid、Doxycycline、Pseudoephedrine、Amphetamine、Dextroamphetamine

仿單警語與禁忌資料尚缺，請參考原廠仿單。

---

## 結論與下一步

**決策：**
- **排名第 1（家族性內臟肌病變）：Hold**
- **腎結石：Proceed with Guardrails**（此為既有用途的延伸佐證，並非全新再利用）

**理由：**
- 排名第 1 的預測僅來自模型分數，無試驗、無文獻，且機轉上無合理連結。
- 腎結石機轉合理，已有統合分析與多項試驗，但多數試驗為小型、替代指標研究，且對磷酸鈣結石有需審慎之處。

**若要推進需要：**
- 取得香港仿單的警語、禁忌與核准適應症文字
- 補充作用機轉資料
- 針對腎功能不全、高血鉀風險族群（如併用保鉀利尿劑、ACEI／ARB）制定血鉀與腎功能監測計畫
- 釐清磷酸鈣結石患者的適用性與尿 pH 目標
- 對胱胺酸症、范可尼症候群等支持性用途，需有直接評估檸檬酸鉀的研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

