---
layout: default
title: Sodium Acetate
parent: 僅模型預測 (L5)
nav_order: 691
evidence_level: L5
indication_count: 5
---

# Sodium Acetate
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

# Sodium Acetate：從電解質/酸中毒矯正劑到先天性凝血酶原缺乏症

## 一句話總結

Sodium Acetate 是電解質/pH 緩衝劑，已知用途包括全靜脈營養（TPN）成分與代謝性酸中毒矯正，但完整原適應症資料目前缺失。
TxGNN 模型預測它可能對**先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency)** 有效，
但目前**無任何臨床試驗、無任何文獻**支持這個方向，且模型本身的機轉分析明確指出兩者間**無可辨識關聯**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無登記資料（已知藥理：電解質補充/代謝性酸中毒矯正，用於 TPN） |
| 預測新適應症 | 先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency) |
| TxGNN 預測分數 | 99.98%（排名 819） |
| 證據等級 | L5（僅有模型預測，無實際研究） |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原始 MOA：Data Gap）。根據已知資訊，Sodium Acetate 屬於電解質/pH 緩衝劑類藥物，常用於全靜脈營養（TPN）與代謝性酸中毒矯正。

TxGNN 模型基於知識圖譜關聯性給出高達 99.98% 的預測分數，但這個分數**沒有機轉或臨床證據支撐**。先天性凝血酶原缺乏症是凝血因子（第 II 因子）基因缺陷導致的合成/功能異常疾病，與電解質緩衝功能之間並無已知的生理路徑交集。

本 Evidence Pack 附帶的機轉分析也明確寫道：「無可辨識機轉關聯……無法建立因果假說」。因此這個預測應被視為**純資料驅動的統計關聯**，而非有機轉基礎的再利用假說，需要額外的臨床前或機轉研究才能判斷是否值得進一步investigate。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Sodium Acetate 目前**未在香港上市**，無許可證登記資料。

---

## 安全性考量

目前無法評估安全性——TFDA/藥監局仿單警語與禁忌症資料尚未取得（Data Gap DG001，嚴重度 **Blocking**），此缺口直接阻斷進入 S1 安全性初評階段，需先取得原廠仿單 PDF 並解析後才能補上。

藥物交互作用查詢結果：無資料（query_status: not_found）。

---

## 其他候選適應症（同批評估，均為 Hold）

本次 Evidence Pack 同時評估了另外 4 個 TxGNN 高分預測，結論一致為證據薄弱、機轉不明：

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 備註 |
|------|------|-----------|---------|------|
| 2 | Epiglottitis（會厭炎） | 99.77% | L5 | 無機轉關聯，無證據 |
| 3 | Urinary tract infection | 99.69% | L4 | 有 2 試驗 + 1 文獻，但**皆與 sodium acetate 或 UTI 主要終點無關**（藥物錯配、指標不符） |
| 4 | Sclerosing cholangitis（硬化性膽管炎） | 99.61% | L5 | 無機轉關聯，無證據 |
| 5 | Gonococcal urethritis（淋病性尿道炎） | 99.57% | L5 | 無抗菌機轉基礎，無證據 |

第 3 名 UTI 雖有查到試驗與文獻，但經人工比對後判定為**誤配訊號**（NCT01808261 藥物為 GSK249320、NCT04302467 為手術輸液策略研究、PMID 34792197 探討的是 crocetin），不構成真實支持證據。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 5 個候選適應症證據等級均為 L4-L5，decision_stage 皆停在 S0，主推的先天性凝血酶原缺乏症無任何臨床試驗或文獻支持，且機轉分析明確排除關聯性。
- 藥物於香港未上市（0 張許可證），且仿單警語/禁忌屬 Blocking 級資料缺口，尚無法進行基本安全性初評。

**若要推進需要：**
- 補齊 TFDA/藥監局仿單完整安全性資訊，解除 DG001（Blocking）
- 取得 DrugBank 完整 MOA 資料，解除 DG002（High），重新評估機轉關聯性
- 若後續仍找不到機轉或臨床證據支持任一候選適應症，建議終止此藥物的再利用評估，不投入進一步資源
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

