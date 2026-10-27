---
layout: default
title: Rasburicase
parent: 僅模型預測 (L5)
nav_order: 760
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Rasburicase：預測新適應症為腎性低尿酸血症 (Hypouricemia, Renal)（證據等級 L5）。原適應症：高尿酸血症"
monitor_inn: "RASBURICASE"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "hepatic porphyria", "early-onset familial noncirrhotic portal hypertension", "primitive portal vein thrombosis"]
---

# Rasburicase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

## Rasburicase：從高尿酸血症到腎性低尿酸血症（預測）
{: .text-alpha }

## 一句話總結

Rasburicase 是一種重組尿酸氧化酶，原本用於治療高尿酸血症。
TxGNN 模型預測它可能對**腎性低尿酸血症 (Hypouricemia, Renal)** 有效，但目前**沒有任何臨床試驗或文獻**支持，且機轉上與預測方向相互矛盾。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高尿酸血症（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 腎性低尿酸血症 (Hypouricemia, Renal) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫未提供 MOA）。根據已知藥理，Rasburicase 是重組尿酸氧化酶，能把尿酸轉化為尿囊素，因此可降低血中尿酸。

然而，腎性低尿酸血症的本質是腎臟尿酸再吸收缺陷（例如 SLC22A12/URAT1 或 SLC2A9 變異），患者血中尿酸本來就偏低。再進一步降低尿酸，無法修正根本缺陷，反而可能增加運動後急性腎損傷與泌尿道結石的風險。

因此，**這個高分預測在機轉上不合理，較可能是知識圖譜的網路鄰近性假象**。同時預測的其他疾病中，只有「次黃嘌呤鳥嘌呤磷酸核糖轉移酶部分缺乏症」（HPRT 部分缺乏，Kelley-Seegmiller 症候群）在機轉上有一定合理性，因為其特徵是尿酸過量生成。但這類疾病的長期治療通常使用 allopurinol 或 febuxostat，Rasburicase 為注射劑、僅限急性短期使用，重複給藥有免疫原性風險，且 G6PD 缺乏者禁用。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-49808 | FASTURTEC FOR INJ 1.5MG（Sanofi Hong Kong Limited） | 未載明 | 未載明 |

---

## 安全性考量

- **藥物交互作用**：共查得 13 項，其中 **2 項為重大 (Major)**：
  - Prilocaine
  - Nitrous acid（亞硝酸）
- 其餘 11 項為中度 (Moderate)，主要是局部或眼用麻醉劑類：Tetracaine（眼用／外用）、Lidocaine（外用／眼用）、Benzocaine、Cocaine（外用／鼻用）、Proparacaine、Oxybuprocaine、Cinchocaine，另有 Idelalisib。
- 補充（來自預測理由分析）：G6PD 缺乏者禁用；重複給藥有免疫原性風險。

警語與禁忌症的仿單資料目前缺漏，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測的證據等級皆為 L5，僅有模型分數，無任何臨床試驗或文獻。
- 排名第一的腎性低尿酸血症在機轉上與藥物作用方向相反，且有潛在風險，應視為模型假象。

**若要推進需要：**
- 取得香港仿單的警語、禁忌症與核准適應症文字（目前為阻斷性資料缺口）。
- 補齊作用機轉資料。
- 若要探索，應優先評估 HPRT 部分缺乏症中的急性重度高尿酸血症情境，先做文獻回顧與病例搜尋。
- 對腎性低尿酸血症、肝性紫質症、門脈高壓與門靜脈血栓等預測，建議不再投入資源，除非有新的機轉證據。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

