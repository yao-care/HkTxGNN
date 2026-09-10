---
layout: default
title: Remdesivir
parent: 僅模型預測 (L5)
nav_order: 640
evidence_level: L5
indication_count: 10
---

# Remdesivir
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

# Remdesivir：原適應症資料缺口 → 多重內分泌腫瘤（MEN）等 10 項預測適應症評估

## 一句話總結

Remdesivir 為核苷酸類似物抗病毒藥物，本次 Evidence Pack 缺少原適應症與作用機轉（MOA）資料，且藥物尚未於香港上市。TxGNN 對此藥物預測了 10 個候選新適應症，分數最高者為**多重內分泌腫瘤 (Multiple Endocrine Neoplasia)**（99.50%），但經逐一檢視證據後，10 項預測**無一項**通過最基本的機轉合理性或證據品質檢驗——多數為零證據雜訊，部分甚至是臨床試驗/文獻的**疾病標籤錯配**（例如標記為「HIV」的 23 個試驗與 20 篇文獻，內容實際上全數是 remdesivir 治療 COVID-19）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 尚無記錄（資料未提供，見 DG001/DG002） |
| 預測新適應症（Rank 1） | 多重內分泌腫瘤 (Multiple Endocrine Neoplasia) |
| TxGNN 預測分數 | 99.50% |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Remdesivir 的詳細作用機轉（MOA）資料，本 Evidence Pack 也未提供原適應症資訊。根據既有的公開藥理知識脈絡，remdesivir 屬核苷酸類似物前驅藥，標靶 RNA 依賴性 RNA 聚合酶（RdRp）。

但就本次排名第一的預測——多重內分泌腫瘤（MEN）——其本質是 RET/MEN1 基因突變導致的遺傳性內分泌腫瘤症候群，與抗病毒藥物的 RdRp 抑制機轉**沒有任何已知生物學關聯**。該候選項無任何臨床試驗或文獻支持（0 筆），評估判斷此為 TxGNN 嵌入相似度產生的高分雜訊（false positive）可能性高，機轉上不具合理性。

換言之，這個預測分數雖高，但**證據品質與機轉合理性均不足**，不建議以此作為推進依據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Remdesivir 目前**未於香港上市**，無許可證登記資料可供列示。

---

## 其他預測適應症總覽（Rank 2–10，補充脈絡）

由於本 Evidence Pack 涵蓋 10 個預測候選（candidate_id 標示為 multi），以下彙整其餘 9 項的證據概況，供整體風險評估參考：

| Rank | 預測適應症 | TxGNN 分數 | 試驗/文獻數 | 證據等級 | 評估結論 |
|------|-----------|-----------|------------|---------|---------|
| 2 | HIV infectious disease | 99.32% | 23 試驗 / 20 文獻 | L5 | **標籤錯配**：全數內容為 remdesivir 治療 COVID-19 的證據，與 HIV 無關（HIV 靠反轉錄酶複製，非 RdRp） |
| 3 | feline acquired immunodeficiency syndrome | 99.07% | 0 / 0 | L5 | 機轉無關聯，純雜訊 |
| 4 | simian immunodeficiency virus infection | 99.07% | 0 / 0 | L5 | 與 #3 分數完全相同，判斷為知識圖譜結構相似節點連動預測，非獨立藥理證據 |
| 5 | 罕見神經發育疾病（皮質白質減少症候群） | 99.03% | 0 / 0 | L5 | 機轉無關聯，純雜訊 |
| 6 | homozygous familial hypercholesterolemia | 99.03% | 0 / 0 | L5 | 機轉無關聯，純雜訊 |
| 7 | Prinzmetal angina | 98.34% | 0 / 0 | L5 | 機轉無關聯，純雜訊 |
| 8 | leprosy | 97.37% | 0 / 5 文獻 | L5 | **標籤錯配**：文獻內容為抗痲瘋病藥物 clofazimine 被重新定位抗 SARS-CoV-2/MERS-CoV 的體外研究，方向相反，非 remdesivir 治療痲瘋病證據 |
| 9 | antithrombin deficiency type 2 | 97.25% | 0 / 0 | L5 | 機轉無關聯，純雜訊 |
| 10 | cytomegalovirus infection | 97.08% | 0 / 9 文獻 | L4 | 文獻多為 COVID-19 住院患者合併 CMV 再活化的**觀察性共病現象**，非 remdesivir 對 CMV 直接抗病毒活性證據；CMV 複製依賴 DNA 聚合酶，與 remdesivir 標靶的 RdRp 不同酶系統 |

**觀察重點**：10 項預測中有 3 項（Rank 2、8、10）在證據收集階段抓到看似「有數量」的試驗/文獻，但逐一核對內容後確認為**疾病標籤錯配或間接共病關聯**，並非真正支持該適應症的證據。這顯示此候選藥物的證據收集流程在疾病命名消歧（disease disambiguation）上存在系統性風險，建議後續預測輸出前加入標題/摘要層級的相關性二次過濾。

---

## 安全性考量

安全性資訊請參考原廠仿單。（本 Evidence Pack 中 TFDA 仿單警語/禁忌資料缺口已標記為 Blocking 等級，直接阻擋進入 S1 安全性初評階段。）

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的預測（多重內分泌腫瘤）雖 TxGNN 分數高達 99.50%，但機轉上與 remdesivir 的抗病毒作用完全無關聯，且無任何臨床試驗或文獻支持，證據等級僅 L5。
- 檢視全部 10 項預測後，證據品質最佳者（CMV, L4）也僅為間接共病觀察，非直接療效證據；另有 2 項（HIV、leprosy）的證據實為疾病標籤錯配，需排除。
- 原適應症、MOA、TFDA 安全性資料均為缺口，其中仿單警語/禁忌屬 Blocking 等級，已直接阻擋進入下一階段評估。

**若要推進需要：**
- 補齊 Remdesivir 原適應症與 MOA 資料（DrugBank API 查詢，DG002）
- 取得 TFDA 仿單警語與禁忌症資料，解除 S1 安全性初評阻擋（DG001）
- 若仍要探索 MEN 或其他候選適應症，需先進行體外/體內機轉驗證研究，目前無任何實證基礎支持人體試驗
- 修正證據收集流程的疾病標籤比對邏輯，避免 HIV/leprosy 類型的錯配案例再次發生
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

