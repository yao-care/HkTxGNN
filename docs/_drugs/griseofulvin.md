---
layout: default
title: Griseofulvin
parent: 僅模型預測 (L5)
nav_order: 420
evidence_level: L5
indication_count: 5
---

# Griseofulvin
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

# Griseofulvin：從抗黴菌用藥到蠅蛆症 (Myiasis)

## 一句話總結

Griseofulvin 是一種抗黴菌藥，香港已有多張藥品許可證。
TxGNN 模型預測它可能對**蠅蛆症 (Myiasis)** 有效，但目前**沒有任何臨床試驗**，只有 **1 篇**關聯性不明的舊文獻。這個預測很可能是知識圖譜的假象，不建議推進。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明（藥理上屬抗黴菌藥） |
| 預測新適應症 | 蠅蛆症 (Myiasis) |
| TxGNN 預測分數 | 99.41% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 9 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 griseofulvin 是抗黴菌藥，透過干擾真菌微管與有絲分裂發揮作用。

但這與蠅蛆症（蠅類幼蟲寄生於皮膚或傷口）之間**沒有合理的藥理關聯**。Griseofulvin 對雙翅目幼蟲沒有已知的活性。0.994 的高分很可能來自知識圖譜中「寄生性皮膚病」鄰近節點的關聯，而非真正的藥理依據。

蠅蛆症的標準處置是移除幼蟲，並搭配 ivermectin 等抗寄生蟲藥物，這些藥物的作用途徑與 griseofulvin 完全不同。

### 其他預測適應症

| 預測適應症 | TxGNN 分數 | 證據 | 評估 |
|-----------|-----------|------|------|
| 癤性蠅蛆症 (Furuncular myiasis) | 99.34% | 無 | 僅為預測，無藥理依據，Hold |
| 傷口蠅蛆症 (Wound myiasis) | 99.34% | 無 | 僅為預測，處置以清創與抗寄生蟲治療為主，Hold |
| 匐行性蠅蛆症 (Creeping myiasis) | 99.34% | 無 | 無抗幼蟲機轉，現有療法（ivermectin、albendazole）途徑不同，Hold |
| 細粒棘球絛蟲感染 (*Echinococcus granulosus*) | 99.32% | 無 | 屬「研究問題」，見下方說明 |

**細粒棘球絛蟲感染**是唯一有假說層級關聯的項目。Griseofulvin 干擾真菌微管，而 benzimidazole 類藥物（albendazole、mebendazole）正是靠作用於寄生蟲微管蛋白治療棘球蚴病。Griseofulvin 是否對該蟲的微管蛋白有活性，目前完全未經檢驗，而且已有有效的核准療法。若要研究，第一步應是體外的殺原頭節或微管蛋白結合試驗，而非臨床評估。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [4098614](https://pubmed.ncbi.nlm.nih.gov/4098614/) | 1970 | Review | The Veterinary Record | 犬貓寄生蟲性皮膚病綜述。無摘要可供判讀，未見 griseofulvin 對蠅蛆症有效的直接證據 |

其餘預測適應症目前無相關文獻。

---

## 香港上市資訊

香港共有 9 張許可證，以下列出 5 張。資料中未載明劑型與核准適應症。

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-34137 | GRISEOFULVIN TAB 125MG (VICKMANS) | Vickmans Laboratories Ltd |
| HK-33380 | GRISEOFULVIN TAB 500MG | APT Pharma Limited |
| HK-26326 | FUYOU TAB 500MG | Wilcome Pharmaceutical Co Ltd |
| HK-66191 | NACOSIL GRISEOFULVIN TABLETS 250MG | Welldone Pharmaceuticals Limited |
| HK-31024 | MEDOFULVIN 125 TAB 125MG | Star Medical Supplies Ltd |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 蠅蛆症的四個預測適應症都只有模型分數，沒有臨床試驗、實質文獻，也沒有合理的作用機轉。高分應視為知識圖譜的假象。
- 現有標準療法明確有效，且 griseofulvin 缺乏抗幼蟲活性，沒有推進的理由。

**若要推進需要：**
- 取得香港衛生署核准的仿單，確認原適應症、警語與禁忌
- 補齊 griseofulvin 的作用機轉資料
- 僅針對細粒棘球絛蟲感染這個研究問題：先做體外殺原頭節或微管蛋白結合試驗，確認有活性後才考慮進一步評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

