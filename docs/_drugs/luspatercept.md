---
layout: default
title: Luspatercept
parent: 僅模型預測 (L5)
nav_order: 468
evidence_level: L5
indication_count: 10
---

# Luspatercept
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Luspatercept：多重疾病老藥新用初篩 — Beta-thalassemia 驗證陽性，其餘 9 項證據薄弱

## 一句話總結

Luspatercept（原廠商品名 Reblozyl）作用機轉為 activin receptor type IIB ligand trap，抑制 GDF11/SMAD2-3 訊號，促進紅血球晚期成熟，原核准用於改善 beta-thalassemia 相關無效造血之貧血。TxGNN 針對本藥物產出 **10 個候選適應症**，其中僅 **Beta-thalassemia, beta+, silent allele** 達到 **L1 證據等級**、建議「Proceed with Guardrails」——但這其實是原廠已核准的適應症，屬模型「重新辨識已知真相」而非新發現；其餘 9 個候選（含分數最高的 monosomy X）機轉關聯薄弱、臨床試驗與文獻均為 0 筆，判定 Hold。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | Beta-thalassemia 相關輸血依賴型貧血（原廠核准適應症；本資料集港版許可證與 original_moa 皆缺，market_status=未上市） |
| TxGNN 候選適應症數 | 10 個（rank 1–10，score 0.9275–0.9600） |
| 分數最高候選 | Monosomy X（Turner syndrome），score **95.99%**，機轉關聯薄弱 → Hold |
| 證據最強候選 | Beta-thalassemia, beta+, silent allele，score 93.32%，**L1 / S3** → Proceed with Guardrails（實為已知適應症再確認，非新發現） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策（新適應症面向） | **Hold** |

---

## 為什麼這個預測合理？

drug.original_moa 欄位標記為缺失，但候選 #7 的機轉描述中揭露了實際作用機轉：Luspatercept 是 activin receptor type IIB 的 ligand trap，透過抑制 GDF11/SMAD2-3 訊號，促進紅血球晚期成熟、改善無效造血（ineffective erythropoiesis）。這正是 Reblozyl 治療 beta-thalassemia 相關貧血的核准機轉——TxGNN 模型將此適應症排在候選之中，等於正確「復現」了已知真相，可視為模型可信度的一種佐證，但不構成新的老藥新用機會。

其餘 9 個候選中，分數最高的 monosomy X（Turner syndrome）為染色體結構異常之多重器官症候群，與 activin/SMAD 紅血球成熟路徑無明確機轉連結；hepatic infarction、hepatic veno-occlusive disease、peliosis hepatis 三者皆為肝臟血管病理，僅與 luspatercept 已知的血栓栓塞安全性訊號有間接關係，並非治療機轉假說；syndrome with combined immunodeficiency、adenosine deaminase deficiency 屬淋巴球免疫缺陷，機轉不相關；familial apolipoprotein C-II deficiency 為脂蛋白代謝疾病，同樣不相關。唯一具生物學合理性的兩個候選是 pyruvate kinase deficiency of red cells 與 Hb Bart's hydrops fetalis——兩者皆屬慢性溶血/無效造血疾病，理論上與紅血球晚期成熟路徑方向一致，但屬 TxGNN 知識圖譜的間接類比推論，且無臨床試驗或文獻佐證。

**十個候選適應症總覽：**

| Rank | 疾病 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|------|------|-----------|---------|---------|------|
| 1 | Monosomy X | 95.99% | L5 | S0 | Hold |
| 2 | Hepatic infarction | 95.70% | L5 | S0 | Hold |
| 3 | Hepatic veno-occlusive disease | 94.91% | L5 | S0 | Hold |
| 4 | Peliosis hepatis | 94.75% | L5 | S0 | Hold |
| 5 | Syndrome with combined immunodeficiency | 94.28% | L5 | S0 | Hold |
| 6 | Pyruvate kinase deficiency of red cells | 93.84% | L5 | S0 | Hold |
| 7 | Thalassemia, beta+, silent allele | 93.32% | **L1** | **S3** | **Proceed with Guardrails** |
| 8 | Familial apolipoprotein C-II deficiency | 93.05% | L5 | S0 | Hold |
| 9 | Adenosine deaminase deficiency | 92.86% | L5 | S0 | Hold |
| 10 | Hb Bart's hydrops fetalis | 92.75% | L5 | S0 | Hold |

---

## 臨床試驗證據

query_log 顯示，針對全部 10 個候選疾病，ClinicalTrials.gov 與 ICTRP 的查詢結果皆為 0 筆。

目前無相關臨床試驗登記。

**但需特別注意**：候選 #7（beta-thalassemia）的 rationale 明確指出，「此適應症的 clinical_trials/literature 欄位均為 0 筆，與已知真實世界證據不符——研判為資料庫收錄缺漏，非證據不存在」（beta-thalassemia 為 Reblozyl 的核准適應症，實際上有 Phase 3 RCT 支持其核准）。本報告不對此臆測具體試驗編號，僅如實反映此資料落差，建議列為待補資料項。

---

## 文獻證據

同上，query_log 對全部 10 個候選疾病的 PubMed 查詢結果皆為 0 筆。

目前無相關文獻。

同樣地，beta-thalassemia 候選被明確標註為資料庫收錄缺漏而非真實無文獻，其餘 9 個候選則無此警示，可視為真實的證據空白。

---

## 香港上市資訊

本藥物於香港尚未上市（market_status = 未上市，total_licenses = 0），無許可證資料可列。

---

## 安全性考量

安全性資訊請參考原廠仿單。

（key_warnings、contraindications 均為 [Data Gap]，DDI 查詢無結果。meta.data_gaps 標記 TFDA 仿單警語/禁忌為 **Blocking** 等級缺口，直接影響是否能進入 S1 安全性初評。）

---

## 結論與下一步

**決策：Hold**

**理由：**
- 分數最高的候選（monosomy X 及其他 8 項）機轉關聯薄弱，且無任何臨床試驗或文獻支持，證據等級皆為 L5。
- 唯一達到 L1/S3 的候選（beta-thalassemia）並非真正的「新」適應症，而是模型正確復現了原廠已核准用途，不構成老藥新用機會；且本身仿單/安全性資料尚缺（DG001 為 Blocking 等級），連既有適應症的安全性初評都無法進行。

**若要推進需要：**
- 優先補齊 TFDA/香港仿單警語與禁忌症資料（DG001，Blocking，來源：TFDA 官網仿單 PDF）
- 補齐正式 MOA 資料來源查證（DG002，來源：DrugBank API）
- 針對 pyruvate kinase deficiency of red cells、Hb Bart's hydrops fetalis 兩個機轉尚可解釋的候選，另行人工檢索文獻，確認是否同樣屬資料庫收錄缺漏
- 若後續要以 beta-thalassemia 作為（已知適應症）香港上市申請基礎，需走完整送件流程，而非本 TxGNN 老藥新用路徑
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

