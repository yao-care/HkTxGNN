---
layout: default
title: Carbocisteine
parent: 僅模型預測 (L5)
nav_order: 162
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Carbocisteine：預測新適應症為痛風 (Gout)（證據等級 L5）。原適應症：本次整理的資料中未載明"
monitor_inn: "CARBOCISTEINE"
predicted_indications: ["gout"]
---

# Carbocisteine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

## Carbocisteine：從呼吸道黏液異常到痛風
{: .text-alpha }

## 一句話總結

Carbocisteine（羧甲司坦）是黏液溶解劑，在香港已有多張許可證上市。
TxGNN 模型預測它可能對**痛風 (Gout)** 有效，但目前**沒有臨床試驗和文獻**支持，僅有模型預測分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本次整理的資料中未載明 |
| 預測新適應症 | 痛風 (Gout) |
| TxGNN 預測分數 | 0.9967 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 16 張／共 16 張） |
| 許可證數 | 16 張（有效 16 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Carbocisteine 屬於黏液溶解劑，一般認為可調節黏液糖蛋白的分泌，並具有抗氧化與抗發炎特性。

一個推測性的連結是：痛風發作時，尿酸結晶會引發氧化壓力與嗜中性白血球主導的發炎反應，而 carbocisteine 的抗氧化與抗發炎作用理論上可能減輕此反應。**這僅是假說，沒有任何已檢索到的試驗或文獻支持。**

此外，目前沒有證據顯示 carbocisteine 會影響尿酸代謝、黃嘌呤氧化酶 (xanthine oxidase) 或 URAT1。模型的高分是目前唯一的依據，原適應症與痛風之間的關聯性也尚待釐清。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港含本藥成分的許可證包括單一成分與複方製劑，張數與有效張數見本頁快速總覽與「香港上市資訊」的許可證表，以下列出部分主要許可證（核准適應症與劑型欄位於資料中皆未載明；請參考原廠仿單）：

<!-- review:begin hk-lic-20261117-carbocisteine-1 -->

> **查核更正（2026-11-24）**：原文為「資料中共有 14 張有效的單一成分許可證，以下列出 5 張主要許可證（核准適應症與劑型欄位於資料中皆未載明，請參考原廠仿單）：」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊；含本藥成分的許可證包括單一成分與複方製劑，張數見本頁快速總覽與許可證表（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-carbocisteine-1 -->

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-68392 | CABOTIN TABLETS 375MG | 單一成分 | JULIUS CHEN & COMPANY (HK) LIMITED | 有效 |
| HK-34628 | SOLMUX PEDIATRIC SUSP 200MG/5ML | 單一成分 | UNAM CORPORATION LTD | 有效 |
| HK-63122 | UNI-CARBOTINE SYRUP 5%W/V | 單一成分 | EUROPHARM LAB CO LTD | 有效 |
| HK-19872 | MUCOSPECT FOR ADULTS SYRUP 250MG/5ML | 單一成分 | EUROPHARM LAB CO LTD | 有效 |
| HK-62353 | NEO-CARBO SYRUP 250MG/5ML | 單一成分 | EUROPHARM LAB CO LTD | 有效 |

上表列出其中 5 張（共 16 張）。

<!-- licenses:end -->

## 安全性考量

- **知識圖譜標示的禁忌疾病**：活動性消化性潰瘍（此為 TxGNN 知識圖譜中的藥物－疾病禁忌關聯，並非仿單文字，需以仿單確認）。

其他安全性資訊（警語、禁忌症、藥物交互作用）請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前僅有模型預測分數（0.9967），沒有任何臨床試驗或文獻，證據等級為 L5。
- 作用機轉資料缺失，與痛風的機轉連結僅為推測，且與尿酸代謝並無已知關聯。

**若要推進需要：**
- 補齊 carbocisteine 的作用機轉資料與原核准適應症
- 取得香港衛生署仿單，完成警語與禁忌症的安全性篩選（特別是活動性消化性潰瘍，而痛風患者常使用 NSAIDs，需評估胃腸道風險）
- 進行文獻與試驗檢索，並設計前臨床研究（如尿酸結晶誘發的發炎模型）驗證抗發炎假說
- 評估給藥途徑與痛風治療情境的相容性

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-24 | 「資料中共有 14 張有效的單一成分許可證，以下列出 5 張主要許可證（核准適應症」→「香港含本藥成分的許可證包括單一成分與複方製劑，張數（含有效、」 | 更正（2026-11-24 修訂，前版保留於紀錄） | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

