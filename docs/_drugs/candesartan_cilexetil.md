---
layout: default
title: Candesartan Cilexetil
parent: 中證據等級 (L3-L4)
nav_order: 131
evidence_level: L4
indication_count: 5
---

# Candesartan Cilexetil
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Candesartan Cilexetil：從高血壓到惡性腎血管性高血壓

## 一句話總結

Candesartan Cilexetil 是血管收縮素 II 第一型受體拮抗劑（ARB），廣泛用於高血壓及心臟衰竭的治療。TxGNN 模型預測它可能對**惡性腎血管性高血壓 (Malignant Renovascular Hypertension)** 有效，目前具有機轉層面的理論依據，惟尚無直接臨床試驗或文獻支持，且存在重要的安全性反向警示。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓、心臟衰竭（香港未上市，無正式核准紀錄） |
| 預測新適應症 | 惡性腎血管性高血壓 (Malignant Renovascular Hypertension) |
| TxGNN 預測分數 | 99.68% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Candesartan Cilexetil 屬於 ARB（血管收縮素 II 受體拮抗劑）類藥物，透過競爭性阻斷 AT1 受體，抑制 Angiotensin II 所引起的血管收縮、醛固酮分泌及腎小管水鈉滯留，進而達到降低全身血壓的效果。目前本 Evidence Pack 缺乏正式 MOA 文件，以上說明為根據藥理類別所作之推論。

惡性腎血管性高血壓通常源於腎動脈狹窄（Renal Artery Stenosis, RAS），腎臟缺血導致 RAAS 系統過度活化，Renin-Angiotensin 軸失調，進而引發惡性高血壓並造成終端器官損傷。機轉上，ARB 直接截斷 Angiotensin II 的效應訊號，理論上具有降低系統血壓及腎血管壓力的潛力，TxGNN 給予此預測 99.68% 高分，反映知識圖譜中 AT1 通路與腎血管病理的強關聯性。

**⚠️ 重要安全性反向警示**：在雙側腎動脈狹窄或孤立腎合併 RAS 的情況下，Angiotensin II 正常維持出球小動脈（efferent arteriole）張力，一旦被 ARB 阻斷，此代償機制失效，可能急性誘發腎小球濾過率（GFR）驟降，導致急性腎損傷（AKI）。此已知風險是本適應症評估中不可忽視的安全性反向訊號，需在任何推進方案中優先釐清患者族群的腎動脈解剖狀態。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Candesartan Cilexetil 目前在香港**未上市**，藥物管制辦事處（Department of Health）無任何有效許可證登記紀錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **注意**：本 Evidence Pack 存在兩項資料缺口：TFDA 仿單警語/禁忌（DG001，Blocking 級）及作用機轉（DG002，High 級），應於進入正式安全性評估前優先補齊。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 雖給予惡性腎血管性高血壓高達 99.68% 的預測分數，機轉層面亦存在 AT1 通路的理論連結（L4 等級），但目前完全缺乏針對此適應症的臨床試驗或直接文獻支持，且在腎動脈狹窄患者族群中使用 ARB 具有明確的 AKI 誘發風險，安全性資料亦尚待補全，不宜在現階段推進。

**若要推進需要：**
- 補齊 MOA 正式文件（查詢 DrugBank API，填補 DG002）
- 取得香港/TFDA 仿單警語與禁忌症全文（填補 DG001，Blocking 級，為進入 S1 安全性評估的前提條件）
- 以「Candesartan + renovascular hypertension」及「ARB + malignant hypertension + renal」為關鍵字進行系統性 PubMed 文獻回顧
- 評估患者篩查策略：腎動脈影像確認是否存在雙側 RAS，以界定可安全使用 ARB 的目標族群
- 參考同類 ARB（如 Losartan、Valsartan）在類似腎血管性高血壓適應症的間接臨床證據，作為佐證資料
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

