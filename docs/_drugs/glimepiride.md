---
layout: default
title: Glimepiride
parent: 僅模型預測 (L5)
nav_order: 409
evidence_level: L5
indication_count: 5
---

# Glimepiride
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

# Glimepiride：從降血糖藥（磺醯脲類）到僵人症候群

## 一句話總結

Glimepiride 是磺醯脲類（sulfonylurea）降血糖藥，香港已有 19 張許可證。
TxGNN 模型預測它可能對**典型僵人症候群 (Classic Stiff Person Syndrome)** 有效。
目前**沒有任何臨床試驗或文獻**支持，這只是模型層級的假說。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 典型僵人症候群 (Classic Stiff Person Syndrome) |
| TxGNN 預測分數 | 99.75% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 19 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。一般認為 Glimepiride 是磺醯脲類藥物，透過阻斷胰臟 β 細胞的 K-ATP 通道來促進胰島素分泌。提供的資料中，香港許可證也未載明核准適應症文字。

僵人症候群是與 GABA 神經傳導及 GAD65 相關的自體免疫疾病，常合併糖尿病。這個預測分數很可能來自知識圖譜中「糖尿病」與「GAD 自體免疫」的鄰近關係，而非治療機轉。**現有資料不支持兩者之間存在直接的機轉連結**，此處僅為假說。

同批預測還包括以下幾項，證據同樣是 L5，且都不支持直接治療效果：

- **局部僵硬肢症候群（Focal Stiff Limb Syndrome）**：分數與僵人症候群完全相同（99.75%），應是同一疾病譜系的圖譜鄰近效應。
- **Opsismodysplasia**：與 INPPL1 (SHIP2) 變異有關，SHIP2 參與胰島素/PI3K 訊號，可能造成圖譜關聯。沒有證據顯示 Glimepiride 能改善骨骼病變。
- **硫胺素反應性巨母細胞貧血症候群（Thiamine-responsive dysfunction syndrome）**：此症候群常併發糖尿病，降血糖藥在概念上只對這一項表現相關。它無法處理貧血或耳聾，也沒有提供使用磺醯脲的報告，充其量只是症狀性的血糖管理。
- **藥物誘發局部脂肪失養症（Drug-induced localized lipodystrophy）**：常與注射胰島素有關，預測應反映糖尿病的圖譜鄰近性。Glimepiride 不能逆轉脂肪失養，即使用來取代注射藥物，也只算糖尿病管理。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共 19 張許可證，以下列出 5 張主要許可證。資料中未提供劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-42323 | AMARYL TAB 2MG | SANOFI HONG KONG LIMITED |
| HK-62478 | LIMERAL TABLETS 4MG | TEVA PHARMACEUTICAL HONG KONG LIMITED |
| HK-67944 | SYNARYL TABLETS 4MG | SYNCO (H.K.) LIMITED |
| HK-58694 | APO-GLIMEPIRIDE TAB 2MG | HIND WING CO LTD |
| HK-56396 | SUCRYL TAB 2MG | ZENFIELDS (H.K.) LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都只有模型分數（證據等級 L5），沒有臨床試驗或文獻。
- 機轉上沒有支持的連結，分數應是來自糖尿病相關的圖譜鄰近性。

**若要推進需要：**
- 取得香港衛生署 (Department of Health) 仿單，補齊警語與禁忌症，這是進入安全性篩選前的必要資料。
- 從 DrugBank 補齊作用機轉 (MOA) 資料。
- 檢索僵人症候群與 Glimepiride/磺醯脲類的文獻和試驗，確認是否有任何實際證據。
- 若要評估其他預測（如硫胺素反應性巨母細胞貧血症候群），需另外查證磺醯脲在該情境的使用報告，並釐清目標是症狀管理還是疾病修飾。

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

