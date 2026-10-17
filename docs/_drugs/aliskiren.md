---
layout: default
title: Aliskiren
parent: 僅模型預測 (L5)
nav_order: 38
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Aliskiren：預測新適應症為原因不明的多因素肺動脈高壓（pulmonary hypertension with unclear multifactorial mech…（證據等級 L5）。原適應症：高血壓"
monitor_inn: "ALISKIREN"
predicted_indications: ["malignant hypertensive renal disease", "chronic pulmonary heart disease", "cerebrovascular disorder"]
---

# Aliskiren
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

# Aliskiren：從高血壓到肺動脈高壓

## 一句話總結

Aliskiren 是一種直接腎素抑制劑，原本用於治療高血壓。
TxGNN 模型預測它可能對**肺動脈高壓（pulmonary hypertension with unclear multifactorial mechanism）**有效，但目前這個適應症**沒有臨床試驗或文獻**支持，僅是模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓（hypertension；香港許可證未載明適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 原因不明的多因素肺動脈高壓（pulmonary hypertension with unclear multifactorial mechanism） |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA）。已知 Aliskiren 是直接腎素抑制劑，作用在腎素－血管張力素－醛固酮系統（RAAS）的第一個限速步驟，降低整個系統的活性。

RAAS 可能影響肺血管的張力與重塑，因此從機轉上推測，抑制腎素有可能影響肺動脈高壓。不過這只是機轉上的合理推論，並無任何臨床試驗或文獻直接驗證。

同一份預測清單中，另有幾個與肺部或缺氧相關的預測：

- **肺疾病或缺氧所致肺動脈高壓**（分數同為 99.98%）：有一篇大鼠研究（PMID 32982180）指出，Aliskiren 對慢性間歇性缺氧引起的心房重塑可能有保護作用。但該研究談的是心房重塑，並非肺動脈高壓本身。
- **慢性肺心病**（分數 99.78%）：僅有一篇 2007 年的研討會試驗摘要，與 Aliskiren 無直接關係。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-60309 | RASILEZ TAB 150MG (ITALY) | 未提供 | 未提供 |
| HK-60310 | RASILEZ TAB 300MG (ITALY) | 未提供 | 未提供 |

兩張許可證均為單方製劑，狀態有效，持證商為 LEE'S PHARMACEUTICAL (H.K) LIMITED。

---

## 安全性考量

- **知識圖譜中的禁忌疾病**（來自藥物－疾病關聯資料，並非仿單文字，僅供參考）：
  - 肝臟：肝衰竭、肝病、肝性腦病變、肝昏迷
  - 胰膽：胰臟炎、膽囊疾病
  - 血管水腫類：血管性水腫（含後天性、遺傳性、RAAS 阻斷劑誘發）
  - 腎臟：無尿、腎動脈阻塞、腎功能不全
  - 代謝與電解質：糖尿病、糖尿病酮酸中毒、缺鉀、高鈣血症、腎鈣質沉著症、磷代謝疾病、副甲狀腺機能亢進、纖維性骨炎、痛風、高尿酸血症
  - 血液：嗜中性白血球低下、顆粒球缺乏症
  - 其他：低血壓、全身性紅斑性狼瘡、新生兒黃疸
- **藥物交互作用**：資料庫共有 100 筆交互作用，以下為部分中度等級：
  - 鉀製劑（氯化鉀、檸檬酸鉀、葡萄糖酸鉀、碳酸氫鉀）
  - SGLT2 抑制劑（Canagliflozin、Dapagliflozin、Empagliflozin、Ertugliflozin）
  - 類固醇（Hydrocortisone、Prednisolone、Prednisone、Dexamethasone、Betamethasone、Budesonide）
  - 其他：Acetylsalicylic acid、Clarithromycin、Aprepitant、Eliglustat、Clotrimazole、Miconazole
- 另外，文獻（PMID 23418282）討論 ALTITUDE 試驗中與 Aliskiren 相關的低血壓與缺血性中風，使用時需留意。

港版仿單的警語與禁忌尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅來自模型分數，沒有臨床試驗與文獻支持，證據等級為 L5。
- 相關肺部、缺氧的研究只有動物或機轉層面的間接資料。香港仿單的安全性資料也尚未取得。

**若要推進需要：**
- 取得 Aliskiren 的作用機轉資料，並檢視其與肺血管重塑的關聯。
- 針對肺動脈高壓進行系統性文獻檢索，並進行動物模型驗證。
- 下載並解析香港衛生署的仿單，完成安全性初步篩查。
- 確認肺動脈高壓族群的血壓、腎功能與血鉀風險，因為該族群本身可能有低血壓的問題。

---

**補充觀察（證據較多的其他預測）：** 在同一份預測清單中，**腦血管疾病**（分數 99.19%）的證據相對較多，包括 1 個已終止的 Phase 2/3 動脈粥樣硬化 MRI 試驗（NCT01417104，71 人，樣本不足）和多篇動物中風研究，證據等級為 L3，建議列為研究問題。若要優先推進，這個方向值得另行評估。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

