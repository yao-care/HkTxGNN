---
layout: default
title: Vildagliptin
parent: 僅模型預測 (L5)
nav_order: 935
evidence_level: L5
indication_count: 9
monitor_inn: "VILDAGLIPTIN"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
last_modified_at: 2026-10-28
description: "Vildagliptin：預測新適應症為局部僵硬肢症候群 (Focal Stiff Limb Syndrome)（證據等級 L5）。原適應症：第 2 型糖尿病"
---

# Vildagliptin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Vildagliptin：從第 2 型糖尿病到局部僵硬肢症候群
{: .text-alpha }

## 一句話總結

Vildagliptin 是一種 DPP-4 抑制劑，知識圖譜中記錄的原適應症為第 2 型糖尿病。
TxGNN 模型預測它可能對**局部僵硬肢症候群 (Focal Stiff Limb Syndrome)** 有效，
但目前**沒有任何臨床試驗或直接相關文獻**支持這個預測，僅屬模型推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 第 2 型糖尿病（知識圖譜中記錄的關聯；本次整理的香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 局部僵硬肢症候群 (Focal Stiff Limb Syndrome) |
| TxGNN 預測分數 | 0.9988 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 19 張／共 19 張） |
| 核准許可證數 | 19 張（有效 19 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Vildagliptin 屬於 DPP-4（二肽基肽酶-4）抑制劑，藥理資料顯示其作用標的包括 DPP4、DPP8、DPP9 與 TRPV4。此類藥物主要透過增強腸促胰島素活性，改善血糖控制。

局部僵硬肢症候群屬於僵人症候群譜系，病理多與自體免疫及中樞神經抑制性（GABA 能）功能異常有關。本次整理的資料中，沒有任何文獻或試驗說明 DPP-4 抑制與此病理之間的關聯，因此**無法建立機轉連結**。

此預測的分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。排名第 2 的經典僵人症候群分數完全相同（0.9988），顯示模型可能將兩者視為相近的疾病，而非各自獨立的證據。一個純屬推測的角度是：僵人症候群常伴隨抗 GAD 自體免疫及糖尿病，但這並未獲得任何 Vildagliptin 相關研究支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

本藥於香港共有 19 張有效許可證，均為單一成分登記。以下列出 5 張主要許可證（許可證資料未載明核准適應症文字及劑型）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-57309 | GALVUS TAB 50MG | 未載明 | 未載明 |
| HK-63165 | GALVUS TABLET 50MG | 未載明 | 未載明 |
| HK-68953 | VILDAGLIPTIN TABLETS 50MG | 未載明 | 未載明 |
| HK-68157 | VILDAGLIPTINA PENTAFARMA CAPSULES 50MG | 未載明 | 未載明 |
| HK-68118 | VILDAGUS TABLETS 50MG | 未載明 | 未載明 |

## 安全性考量

- **藥物作用標的／交互作用資料**：藥理資料顯示 Vildagliptin 作用於 DPP4、DPP8、DPP9 與 TRPV4，此為標的結合資訊，並非具臨床分級的藥物交互作用。

其餘警語與禁忌症資料不足，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數，沒有任何臨床試驗或針對此疾病的文獻，證據等級為 L5，且機轉上缺乏合理連結。
- 同批預測的其他疾病（如脂肪營養不良各亞型、胰臟發育不全）也有相近的高分，這些分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據或真實療效訊號。

**若要推進需要：**
- 取得 Vildagliptin 的作用機轉資料，並評估與僵人症候群譜系病理的關聯
- 進行系統性文獻檢索，確認是否有任何 DPP-4 抑制劑用於此類疾病的研究或病例
- 取得香港衛生署仿單，補齊警語與禁忌症資料
- 在有任何前臨床或病例層級證據之前，不建議投入臨床開發
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

