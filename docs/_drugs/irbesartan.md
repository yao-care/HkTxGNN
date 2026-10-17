---
layout: default
title: Irbesartan
parent: 僅模型預測 (L5)
nav_order: 483
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Irbesartan：預測新適應症為惡性腎血管性高血壓 (Malignant Renovascular Hypertension)（證據等級 L5）。原適應症：高血壓、糖尿病腎病變"
monitor_inn: "IRBESARTAN"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
---

# Irbesartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Irbesartan：從高血壓與糖尿病腎病變到惡性腎血管性高血壓

## 一句話總結

Irbesartan 是血管張力素 II 第一型受體阻斷劑（ARB），原本用於高血壓及糖尿病腎病變。
TxGNN 模型預測它可能對**惡性腎血管性高血壓 (Malignant Renovascular Hypertension)** 有效，
但目前**沒有相關臨床試驗與文獻**，僅有模型預測分數支持。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓、糖尿病腎病變（香港許可證未提供適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 惡性腎血管性高血壓 (Malignant Renovascular Hypertension) |
| TxGNN 預測分數 | 99.31% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Irbesartan 屬於 ARB 類藥物，透過阻斷血管張力素 II 第一型受體來降低血壓、保護腎臟，其在高血壓與糖尿病腎病變中的療效已被證實。

腎血管性高血壓主要由腎素－血管張力素系統（RAS）過度活化所驅動，因此阻斷此路徑在機轉上具合理性，且與已核准的高血壓適應症高度相關。

但需特別留意：ARB 用於腎血管疾病時有已知風險，例如雙側腎動脈狹窄可能導致急性腎功能惡化。此外，同為高分數的「惡性高血壓性腎病」（99.31%）與本預測分數完全相同，顯示可能來自圖譜上共通的訊號，而非獨立證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

> 補充：同一藥物的其他預測適應症中，「低氧相關肺高血壓 (Pulmonary hypertension owing to lung disease and/or hypoxia)」有 11 篇檢索文獻，但多為動物或細胞的前臨床研究，且部分與 irbesartan 無關（如中藥萃取物、roxadustat 過量病例報告），屬 L4 證據，僅能視為研究問題，不屬於本報告主要預測。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-64347 | EURBESAR TABLETS 300MG | 錠劑 | 未提供 |
| HK-42891 | APROVEL TAB 150MG | 錠劑 | 未提供 |
| HK-64346 | EURBESAR TABLETS 150MG | 錠劑 | 未提供 |
| HK-60779 | CONVERIUM TAB 150MG | 錠劑 | 未提供 |
| HK-67444 | IFIRMASTA TABLETS 150MG | 錠劑 | 未提供 |

（共 20 張有效單方許可證，上表僅列出 5 張。）

## 安全性考量

- **知識圖譜標示的禁忌或需注意疾病**（非仿單內容）：血管性水腫（含遺傳性及 RAS 阻斷劑誘發）、胰臟炎、系統性紅斑狼瘡、肌病變與橫紋肌溶解、低血鉀相關疾病、糖尿病酮酸中毒、低血壓、無尿、腎動脈阻塞、肝性腦病變、高尿酸血症與痛風、高血鈣、腎鈣質沉著症、副甲狀腺機能亢進等。
- **藥物交互作用**：資料庫共 100 筆，其中需特別注意的重大 (Major) 交互作用為**檸檬酸鉀**與**碳酸氫鉀**（高血鉀風險）。中度交互作用包括皮質類固醇（hydrocortisone、dexamethasone、betamethasone、triamcinolone、budesonide）、阿斯匹靈、SGLT2 抑制劑（canagliflozin、dapagliflozin、empagliflozin）、胰島素（aspart、degludec）、bupropion、aprepitant、morphine 等。

其餘警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前僅有模型預測分數（證據等級 L5），沒有針對此適應症的臨床試驗或文獻。
- ARB 在腎血管疾病有已知的腎功能惡化風險，需要更審慎的評估。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌資料，完成安全性篩選
- 補充詳細的作用機轉（MOA）資料
- 系統性搜尋 ARB 於腎血管性高血壓、惡性高血壓的臨床與觀察性研究
- 針對雙側腎動脈狹窄等族群，訂定腎功能與血鉀的監測計畫
- 確認各許可證的核准適應症與劑型資料
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

