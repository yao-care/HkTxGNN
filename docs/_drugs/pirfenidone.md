---
layout: default
title: Pirfenidone
parent: 僅模型預測 (L5)
nav_order: 592
evidence_level: L5
indication_count: 10
---

# Pirfenidone
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

# Pirfenidone：原適應症資料缺失 → 預測新適應症 Extracutaneous Mastocytoma（皮膚外肥大細胞瘤）

## 一句話總結

本次 Evidence Pack 中 Pirfenidone（DrugBank ID: DB04951）的原適應症資料因藥物基本資料缺口尚未提供。TxGNN 模型預測其可能對**皮膚外肥大細胞瘤（Extracutaneous Mastocytoma）**有效，預測分數高達 **99.71%**，但目前**查無任何臨床試驗或文獻佐證**，且模型評估文字本身即註記「與已知機轉無交集，屬純模型預測」。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（未提供許可證或原適應症資訊） |
| 預測新適應症 | Extracutaneous Mastocytoma（皮膚外肥大細胞瘤） |
| TxGNN 預測分數 | 99.71%（排名第 6069） |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 Pirfenidone 詳細的官方作用機轉（MOA）資料（DrugBank 查詢缺口，優先等級 High）。評估紀錄中僅在各候選適應症的機轉推論文字裡提及 Pirfenidone 具抗纖維化、抑制 TGF-β 訊息傳導的特性，但此描述並非正式登錄的 MOA 資料，須另行以 DrugBank API 查證。

由於原適應症資料完全缺失，無法比對原適應症與皮膚外肥大細胞瘤之間的關聯性。

就此候選適應症本身而言，證據並不支持機轉合理性：肥大細胞瘤的病理核心是 KIT 突變驅動的肥大細胞異常增生，與 Pirfenidone 的抗纖維化/抗 TGF-β 機轉**無已知交集**，也**無任何文獻或體外資料**支持此連結——這是模型純統計關聯下的高分預測，尚未有機轉或實證支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 安全性考量

安全性資訊請參考原廠仿單。

（註：本評估目前有一項 Blocking 等級資料缺口——TFDA 仿單警語/禁忌尚未取得，在補齊前無法完成安全性初評。）

## 結論與下一步

**決策：Hold**

**理由：**
此候選適應症證據等級為 L5，無任何臨床試驗或文獻支持，且評估文字本身已明確指出機轉上與已知病理無交集，純屬模型預測，尚無法支持推進。

**若要推進需要：**
- 補齊 TFDA 仿單警語與禁忌資料（DG001，Blocking，需下載並解析仿單 PDF）
- 補齊 Pirfenidone 作用機轉資料（DG002，High，需查詢 DrugBank API）
- 補齊原適應症與香港上市許可證資訊，以利完整比對
- 若仍要在此藥物的候選清單中尋找標的，建議優先參考本次評估中證據等級較高的「fibroblastic neoplasm」（L4，6 篇文獻），但須注意其中一篇文獻報告 Pirfenidone 使用後誘發未分化多形性肉瘤（PMID 29702057），屬安全性負向訊號，需先排除致腫瘤風險再評估再利用可能性
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

